# Copyright (C) 2018 Avatao.com Innovative Learning Kft.
# All Rights Reserved. See LICENSE file for details.

from uuid import UUID

from flask import Blueprint, request, abort

from tmf.dataaccess.data_gateway import create_new_data_flow_model, set_data_flow_name, set_data_flow_description, get_data_flow_model_by_id, set_data_flow_start_point, set_data_flow_end_point, get_component_model_by_id
from tmf.dataaccess.exceptions import InvalidPrimaryKeyError, InvalidTypeError, NotInTheSameSystemError
from tmf.handlers.serialization import DataFlowSerializer
from .create_message import create_message


data_flow_blueprint = Blueprint("data_flow", __name__, url_prefix = "/static")

@data_flow_blueprint.route("/systems/<uuid:system_id>/data_flows/create", methods = ["POST"])
def create(system_id : UUID):
    if not request.json or not "type" in request.json:
        abort(400)

    name = request.json.get("name", "") #TODO default name and description
    description = request.json.get("description", "")

    try:
        data_flow_model = create_new_data_flow_model(system_id = system_id, data_flow_type = request.json["type"], name = name, description = description)
    except InvalidPrimaryKeyError as pkerror:
        abort(404, pkerror)
    except InvalidTypeError as terror:
        abort(400, terror)

    return create_message("data flow created", DataFlowSerializer(data_flow_model).create_one_level_dictionary())

@data_flow_blueprint.route("/data_flows/<uuid:data_flow_id>", methods = ("PUT", "GET"))
def get_properties(data_flow_id: UUID):
    if request.method == "PUT":
        return set_properties(data_flow_id, request)

    try:
        data_flow_model = get_data_flow_model_by_id(data_flow_id)
    except InvalidPrimaryKeyError as error:
        abort(404, error)

    return create_message("sending existing data flow", DataFlowSerializer(data_flow_model).create_full_dictionary())

def set_properties(data_flow_id: UUID, request):
    if not request.json or not "description" in request.json and not "name" in request.json:
        abort(400)

    try:
        if "name" in request.json:
            data_flow_model = set_data_flow_name(data_flow_id, request.json["name"])
        if "description" in request.json:
            data_flow_model = set_data_flow_description(data_flow_id, request.json["description"])
    except InvalidPrimaryKeyError as error:
        abort(404, error)

    return create_message("data flow's properties have been set", DataFlowSerializer(data_flow_model).create_one_level_dictionary())

@data_flow_blueprint.route("/data_flows/<uuid:data_flow_id>/end_point", methods = ("PUT","GET"))
def get_end_point(data_flow_id : UUID):
    if request.method == "PUT":
        return set_end_point(data_flow_id, request)

    try:
        data_flow_model = get_data_flow_model_by_id(data_flow_id)
        component_model = data_flow_model.end_point
    except InvalidPrimaryKeyError as error:
        abort(404, error)

    if component_model is None:
        return create_message("data flow's end point is not connected", "")
    else:
        return create_message("sending data flow's end point", ComponentSerializer(component_model).create_full_dictionary())

def set_end_point(data_flow_id : UUID, request):
    if not request.json or not "component_id" in request.json:
        abort(400)

    try:
        data_flow_model = set_data_flow_end_point(data_flow_id = data_flow_id, component_id = request.json["component_id"])
    except InvalidPrimaryKeyError as error:
        abort(404, error)
    except NotInTheSameSystemError as serror:
            abort(409, serror)

    return create_message("data flow's end point has been connected", {
        "data flow id" : data_flow_model.id_,
        "end point id" :  data_flow_model.end_point.id_
    })

@data_flow_blueprint.route("/data_flows/<uuid:data_flow_id>/start_point", methods = ("PUT","GET"))
def get_start_point(data_flow_id : UUID):
    if request.method == "PUT":
        return set_start_point(data_flow_id, request)

    try:
        data_flow_model = get_data_flow_model_by_id(data_flow_id)
        component_model = data_flow_model.start_point
    except InvalidPrimaryKeyError as error:
        abort(404, error)

    if component_model is None:
        return create_message("data flow's start point is not connected", "")
    else:
        return create_message("sending data flow's start point", ComponentSerializer(component_model).create_full_dictionary())


def set_start_point(data_flow_id : UUID, request):
    if not request.json or not "component_id" in request.json:
        abort(400)

    try:
        data_flow_model = set_data_flow_start_point(data_flow_id = data_flow_id, component_id = request.json["component_id"])
    except InvalidPrimaryKeyError as error:
        abort(404, error)
    except NotInTheSameSystemError as serror:
        abort(409, serror)

    return create_message("data flow's start point has been connected", {
        "data flow id" : data_flow_model.id_,
        "start point id" :  data_flow_model.start_point.id_
    })
