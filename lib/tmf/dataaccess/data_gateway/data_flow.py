# Copyright (C) 2018 Avatao.com Innovative Learning Kft.
# All Rights Reserved. See LICENSE file for details.

from uuid import UUID

from tmf.dataaccess.orm.models import SystemModel
from tmf.dataaccess.orm.models.data_flows import types, DataFlowModel
from tmf.dataaccess.exceptions import InvalidTypeError
from .session import session
from .check_none import check_none
from .system import get_system_model_by_id
from .component import get_component_model_by_id
from .check_same_system import check_component_data_flow_in_same_system


def get_data_flow_model_by_id(id : UUID):
    data_flow_model = session.query(DataFlowModel).get(str(id))
    check_none(data_flow_model, id)

    return data_flow_model

def create_new_data_flow_model(system_id : UUID, name : str, description : str, data_flow_type : str):
    try:
        data_flow_model = types[data_flow_type](name = name, description = description)
    except KeyError:
        raise InvalidTypeError(data_flow_type)

    system_model = get_system_model_by_id(system_id)
    system_model.data_flows.append(data_flow_model)
    session.commit()

    return data_flow_model

def set_data_flow_name(id : UUID, name : str):
    data_flow_model = get_data_flow_model_by_id(id)
    data_flow_model.name = name
    session.commit()

    return data_flow_model

def set_data_flow_description(id : UUID, description : str):
    data_flow_model = get_data_flow_model_by_id(id)
    data_flow_model.description = description
    session.commit()

    return data_flow_model

def set_data_flow_start_point(data_flow_id : UUID, component_id : UUID):
    data_flow_model = get_data_flow_model_by_id(data_flow_id)
    component_model = get_component_model_by_id(component_id)
    check_component_data_flow_in_same_system(component_model = component_model, data_flow_model = data_flow_model)

    data_flow_model.start_point = component_model
    session.commit()

    return data_flow_model

def set_data_flow_end_point(data_flow_id : UUID, component_id : UUID):
    data_flow_model = get_data_flow_model_by_id(data_flow_id)
    component_model = get_component_model_by_id(component_id)
    check_component_data_flow_in_same_system(component_model = component_model, data_flow_model = data_flow_model)

    data_flow_model.end = component_model
    session.commit()

    return data_flow_model
