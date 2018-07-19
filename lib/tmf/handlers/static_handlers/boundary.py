# Copyright (C) 2018 Avatao.com Innovative Learning Kft.
# All Rights Reserved. See LICENSE file for details.

from uuid import UUID

from flask import Blueprint, request, jsonify, abort

from tmf.dataaccess.data_gateway import create_new_boundary_model, set_boundary_name, set_boundary_description, get_boundary_model_by_id
from tmf.dataaccess.exceptions import InvalidPrimaryKeyError


boundary_blueprint = Blueprint("boundary", __name__, url_prefix = "/static")

@boundary_blueprint.route("/systems/<uuid:system_id>/boundaries/create", methods = ["POST"])
def create(system_id : UUID):
    name = "" #TODO default name and description
    description = ""
    if request.json:
        name = request.json.get("name", "")
        description = request.json.get("description", "")

    try:
        boundary_model = create_new_boundary_model(system_id = system_id, name = name, description = description)
    except InvalidPrimaryKeyError as error:
        abort(404, error)

    return jsonify({
        "message" : "boundary created",
        "data" : {
            "id" : boundary_model.id_,
            "name" : boundary_model.name,
            "description" : boundary_model.description
        }
    })

@boundary_blueprint.route("/boundaries/<uuid:boundary_id>", methods = ("PUT", "GET"))
def get(boundary_id: UUID):
    if request.method == "PUT":
        return set_properties(boundary_id, request)

    try:
        boundary_model = get_boundary_model_by_id(boundary_id)
    except InvalidPrimaryKeyError as error:
        abort(404, error)

    return jsonify({
        "message" : "sending existing boundary",
        "data" : {
            "id" : boundary_model.id_,
            "name" : boundary_model.name,
            "description" : boundary_model.description,
            "system id" : boundary_model.system_id,
            "components" : [component.id_ for component in boundary_model.components]
        }
    })

def set_properties(boundary_id: UUID, request):
    if not request.json or not "description" in request.json and not "name" in request.json:
        abort(400)

    try:
        if "name" in request.json:
            boundary_model = set_boundary_name(boundary_id, request.json["name"])
        if "description" in request.json:
            boundary_model = set_boundary_description(boundary_id, request.json["description"])
    except InvalidPrimaryKeyError as error:
        abort(404, error)

    return jsonify({
        "message" : "boundary's properties have been set",
        "data" : {
            "id" : boundary_model.id_,
            "name" : boundary_model.name,
            "description" : boundary_model.description
        }
    })
