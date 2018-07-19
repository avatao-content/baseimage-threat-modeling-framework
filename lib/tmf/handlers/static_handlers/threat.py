# Copyright (C) 2018 Avatao.com Innovative Learning Kft.
# All Rights Reserved. See LICENSE file for details.

from uuid import UUID

from flask import Blueprint, request, jsonify, abort

from tmf.dataaccess.data_gateway import create_new_component_model, set_component_name, set_component_description, get_component_model_by_id
from tmf.dataaccess.exceptions import InvalidPrimaryKeyError


threat_blueprint = Blueprint("threat", __name__, url_prefix = "/static")

@component_blueprint.route("/threat_containers/<uuid:threat_container_id>/threat/create", methods = ["POST"])
def create(threat_container_id : UUID):
    
