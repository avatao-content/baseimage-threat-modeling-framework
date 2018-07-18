# Copyright (C) 2018 Avatao.com Innovative Learning Kft.
# All Rights Reserved. See LICENSE file for details.

from uuid import UUID

from flask import Blueprint, request, jsonify

from tmf.dataaccess.data_gateway import create_new_boundary_model, set_boundary_name, set_boundary_description


boundary_blueprint = Blueprint("boundary", __name__, url_prefix = "/static")

@boundary_blueprint.route("/systems/<uuid:system_id>/create_boundary", methods = ["POST"])
def create(system_id: UUID):
    name = request.json.get("name", "")
    description = request.json.get("description", "")

    boundary_model = create_new_boundary_model(system_id, name = name, description = description)
    return jsonify({
        "message" : "boundary created",
        "data" : {
            "id" : boundary_model.id_,
            "name" : boundary_model.name,
            "description" : boundary_model.description,
            "system id" : boundary_model.system_id
        }
    })

@boundary_blueprint.route("/boundaries/<uuid:boundary_id>/set_name", methods = ["POST"])
def set_name(boundary_id: UUID):
    name = request.json.get("name", "")

    boundary_model = set_boundary_name(boundary_id, name)
    return jsonify({
        "message" : "boundary's name has been set",
        "data" : {
            "id" : boundary_model.id_,
            "name" : boundary_model.name,
            "description" : boundary_model.description,
            "system id" : boundary_model.system_id
        }
    })

@boundary_blueprint.route("/boundaries/<uuid:boundary_id>/set_description", methods = ["POST"])
def set_description(boundary_id: UUID):
    description = request.json.get("description", "")

    boundary_model = set_boundary_description(boundary_id, description)
    return jsonify({
        "message" : "boundary's description has been set",
        "data" : {
            "id" : boundary_model.id_,
            "name" : boundary_model.name,
            "description" : boundary_model.description,
            "system id" : boundary_model.system_id
        }
    })
