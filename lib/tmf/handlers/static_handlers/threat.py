# Copyright (C) 2018 Avatao.com Innovative Learning Kft.
# All Rights Reserved. See LICENSE file for details.

from uuid import UUID

from flask import Blueprint, request, jsonify, abort

from tmf.dataaccess.data_gateway import create_new_threat_model, get_all_threat_models_in_system, get_threat_model_by_id, set_threat_name, set_threat_detected, set_threat_description
from tmf.dataaccess.exceptions import InvalidPrimaryKeyError, InvalidTypeError


threat_blueprint = Blueprint("threat", __name__, url_prefix = "/static")

def full_threat_model_to_dict(threat_model):
    return {
        "id" : threat_model.id_,
        "name" : threat_model.name,
        "description" : threat_model.description,
        "type" : threat_model.type,
        "detected" : threat_model.detected,
        "container" : threat_model.threat_container_id
    }

@threat_blueprint.route("/threat_containers/<uuid:threat_container_id>/threats/create", methods = ["POST"])
def create(threat_container_id : UUID):
    if not request.json or not "type" in request.json:
        abort(400)

    name = request.json.get("name", "") #TODO default name and description
    description = request.json.get("description", "")
    detected = request.json.get("detected", False)

    try:
        threat_model = create_new_threat_model(threat_container_id = threat_container_id, name = name, description = description, detected = detected, threat_type = request.json["type"])
    except InvalidPrimaryKeyError as pkerror:
        abort(404, pkerror)
    except InvalidTypeError as terror:
        abort(400, terror)

    return jsonify({
        "message" : "threat created",
        "data" : full_threat_model_to_dict(threat_model)
    })

@threat_blueprint.route("/threats/<uuid:threat_id>", methods = ("PUT", "GET"))
def get_properties(threat_id: UUID):
    if request.method == "PUT":
        return set_properties(threat_id, request)

    try:
        threat_model = get_threat_model_by_id(threat_id)
    except InvalidPrimaryKeyError as error:
        abort(404, error)

    return jsonify({
        "message" : "sending existing threat",
        "data" : full_threat_model_to_dict(threat_model)
    })

def set_properties(threat_id: UUID, request):
    if not request.json or not "description" in request.json and not "name" in request.json and not "detected" in request.json:
        abort(400)

    try:
        if "name" in request.json:
            threat_model = set_threat_name(threat_id, request.json["name"])
        if "description" in request.json:
            threat_model = set_threat_description(threat_id, request.json["description"])
        if "detected" in request.json:
            threat_model = set_threat_detected(threat_id, request.json["detected"])
    except InvalidPrimaryKeyError as error:
        abort(404, error)

    return jsonify({
        "message" : "threat's properties have been set",
        "data" : full_threat_model_to_dict(threat_model)
    })

@threat_blueprint.route("/systems/<uuid:system_id>/threats")
def get_all_threats_in_system(system_id):
    try:
        threat_models = get_all_threat_models_in_system(system_id)
    except InvalidPrimaryKeyError as error:
        abort(404, error)

    return jsonify({
        "message" : "returning all threats in system",
        "data" : {
            "system id" : system_id,
            "threat" : [full_threat_model_to_dict(threat_model) for threat_model in threat_models]
        }
    })
