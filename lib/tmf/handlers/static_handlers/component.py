# Copyright (C) 2018 Avatao.com Innovative Learning Kft.
# All Rights Reserved. See LICENSE file for details.

from uuid import UUID

from flask import Blueprint, request, jsonify, abort

from tmf.dataaccess.data_gateway import create_new_component_model, set_component_name, set_component_description, get_component_model_by_id
from tmf.dataaccess.exceptions import InvalidPrimaryKeyError


component_blueprint = Blueprint("component", __name__, url_prefix = "/static")

def full_component_model_to_dict(component_model):
    return  {
        "id" : component_model.id_,
        "name" : component_model.name,
        "description" : component_model.description,
        "threats" : [threat.id_ for threat in component_model.threats],
        "inflows" : [inflow.id_ for inflow in component_model.inflows],
        "outflows" : [outflow.id_ for outflow in component_model.outflows],
    }


@component_blueprint.route("/boundaries/<uuid:boundary_id>/components/create", methods = ["POST"])
def create(boundary_id : UUID):
    name = "" #TODO default name and description
    description = ""
    if request.json:
        name = request.json.get("name", "")
        description = request.json.get("description", "")

    try:
        component_model = create_new_component_model(boundary_id = boundary_id, name = name, description = description)
    except InvalidPrimaryKeyError as error:
        abort(404, error)

    return jsonify({
        "message" : "component created",
        "data" : {
            "id" : component_model.id_,
            "name" : component_model.name,
            "description" : component_model.description
        }
    })

@component_blueprint.route("/components/<uuid:component_id>", methods = ("PUT", "GET"))
def get(component_id: UUID):
    if request.method == "PUT":
        return set_properties(component_id, request)

    try:
        component_model = get_component_model_by_id(boundary_id)
    except InvalidPrimaryKeyError as error:
        abort(404, error)

    return jsonify({
        "message" : "sending existing component",
        "data" : full_component_model_to_dict(component_model)
    })

def set_properties(component_id: UUID, request):
    if not request.json or not "description" in request.json and not "name" in request.json:
        abort(400)

    try:
        if "name" in request.json:
            component_model = set_component_name(component_id, request.json["name"])
        if "description" in request.json:
            component_model = set_component_description(component_id, request.json["description"])
    except InvalidPrimaryKeyError as error:
        abort(404, error)

    return jsonify({
        "message" : "component's properties have been set",
        "data" : {
            "id" : component_model.id_,
            "name" : component_model.name,
            "description" : component_model.description
        }
    })
