# Copyright (C) 2018 Avatao.com Innovative Learning Kft.
# All Rights Reserved. See LICENSE file for details.

from uuid import UUID

from flask import Blueprint, request, jsonify

from tmf.dataaccess.data_gateway import create_new_system_model, set_system_name, set_system_description, get_system_model_by_id


system_blueprint = Blueprint("system", __name__, url_prefix = "/static/systems")

@system_blueprint.route("/create", methods = ["POST"])
def create():
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

@system_blueprint.route("/<uuid:system_id>")
def get(system_id: UUID):
    system_model = get_system_model_by_id(system_id)

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

@system_blueprint.route("/<uuid:system_id>/set_name", methods = ["POST"])
def set_name(system_id: UUID):
    name = request.json.get("name", "")

    system_model = set_system_name(system_id, name)
    return jsonify({
        "message" : "system's name has been set",
        "data" : {
            "id" : system_model.id_,
            "name" : system_model.name,
            "description" : system_model.description
        }
    })

@system_blueprint.route("/<uuid:system_id>/set_description", methods = ["POST"])
def set_description(system_id: UUID):
    description = request.json.get("description", "")

    system_model = set_system_description(system_id, description)
    return jsonify({
        "message" : "system's description has been set",
        "data" : {
            "id" : system_model.id_,
            "name" : system_model.name,
            "description" : system_model.description
        }
    })
