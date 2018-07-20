# Copyright (C) 2018 Avatao.com Innovative Learning Kft.
# All Rights Reserved. See LICENSE file for details.

from uuid import UUID

from tmf.dataaccess.orm.models import ThreatContainerModel
from tmf.dataaccess.orm.models.threats import types, ThreatModel
from tmf.dataaccess.exceptions import InvalidTypeError
from .session import session
from .check_none import check_none
from .system import get_system_model_by_id


def get_all_threat_models_in_system(system_id):
    system_model = get_system_model_by_id(system_id)
    threat_models = set() #easy way to prevent duplicates

    for boundary in system_model.boundaries:
        for component in boundary.components:
            threat_models = threat_models.union(component.threats)

    for data_flow in system_model.data_flows:
        threat_models = threat_models.union(data_flow.threats)

    return threat_models

def get_threat_model_by_id(id : UUID):
    threat_model = session.query(ThreatModel).get(str(id))
    check_none(threat_model, id)

    return threat_model

def get_threat_container_model_by_id(id : UUID):
    threat_container_model = session.query(ThreatContainerModel).get(str(id))
    check_none(threat_container_model, id)

    return threat_container_model

def create_new_threat_model(threat_container_id : UUID, name : str, description : str, threat_type : str, detected : bool):
    try:
        threat_model = types[threat_type](name = name, description = description, detected = detected)
    except KeyError:
        raise InvalidTypeError(threat_type)

    threat_container_model = get_threat_container_model_by_id(threat_container_id)
    threat_container_model.threats.append(threat_model)
    session.commit()

    return threat_model

def set_threat_name(id : UUID, name : str):
    threat_model = get_threat_model_by_id(id)
    threat_model.name = name
    session.commit()

    return threat_model

def set_threat_description(id : UUID, description : str):
    threat_model = get_threat_model_by_id(id)
    threat_model.description = description
    session.commit()

    return threat_model

def set_threat_detected(id : UUID, detected : bool):
    threat_model = get_threat_model_by_id(id)
    threat_model.detected = detected
    session.commit()

    return threat_model
