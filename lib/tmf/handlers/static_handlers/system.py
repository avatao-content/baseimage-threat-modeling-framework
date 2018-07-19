# Copyright (C) 2018 Avatao.com Innovative Learning Kft.
# All Rights Reserved. See LICENSE file for details.

from uuid import UUID

from flask import Blueprint, request, jsonify, abort

from tmf.dataaccess.data_gateway import create_new_system_model, set_system_name, set_system_description, get_system_model_by_id
from tmf.dataaccess.exceptions import InvalidPrimaryKeyError


system_blueprint = Blueprint("system", __name__, url_prefix = "/static/systems")

@system_blueprint.route("/create", methods = ["POST"])
def create():
    name = "" #TODO default name and description
    description = ""
    if request.json:
        name = request.json.get("name", "")
        description = request.json.get("description", "")

    system_model = create_new_system_model(name = name, description = description)
    return jsonify({
        "message" : "system created",
        "data" : {
            "id" : system_model.id_,
            "name" : system_model.name,
            "description" : system_model.description
        }
    })

@system_blueprint.route("/<uuid:system_id>", methods = ("PUT", "GET"))
def get(system_id: UUID):
    if request.method == "PUT":
        return set_properties(system_id, request)

    try:
        system_model = get_system_model_by_id(system_id)
    except InvalidPrimaryKeyError as error:
        abort(404, error)

    return jsonify({
        "message" : "sending existing system",
        "data" : {
            "id" : system_model.id_,
            "name" : system_model.name,
            "description" : system_model.description,
            "boundaries" : [boundary.id_ for boundary in system_model.boundaries],
            "data_flows" : [data_flow.id_ for data_flow in system_model.data_flows]
        }
    })

def set_properties(system_id: UUID, request):
    if not request.json or not "description" in request.json and not "name" in request.json:
        abort(400)

    try:
        if "name" in request.json:
            system_model = set_system_name(system_id, request.json["name"])
        if "description" in request.json:
            system_model = set_system_description(system_id, request.json["description"])
    except InvalidPrimaryKeyError as error:
        abort(404, error)

    return jsonify({
        "message" : "system's properties have been set",
        "data" : {
            "id" : system_model.id_,
            "name" : system_model.name,
            "description" : system_model.description
        }
    })
