# Copyright (C) 2018 Avatao.com Innovative Learning Kft.
# All Rights Reserved. See LICENSE file for details.

from uuid import UUID

from tmf.dataaccess.orm.models import DataFlowModel, SystemModel
from .session import session


def create_new_data_flow_model(system_id : UUID, name : str, description : str):
    data_flow_model = DataFlowModel(name = name, description = description)

    system_model = session.query(SystemModel).get(str(system_id))
    system_model.components.append(data_flow_model)
    session.commit()

    return data_flow_model

def set_data_flow_name(id : UUID, name : str):
    data_flow_model = session.query(DataFlowModel).get(str(id))
    data_flow_model.name = name
    session.commit()

    return data_flow_model

def set_data_flow_description(id : UUID, description : str):
    data_flow_model = session.query(DataFlowModel).get(str(id))
    data_flow_model.description = description
    session.commit()

    return data_flow_model

def set_data_flow_start_point(data_flow_id : UUID, component_id : UUID):
    data_flow_model = session.query(DataFlowModel).get(str(data_flow_id))
    component_model = session.query(ComponentModel).get(str(component_id))

    data_flow_model.start_point = component_model
    session.commit()

    return data_flow_model

def set_data_flow_end_point(data_flow_id : UUID, component_id : UUID):
    data_flow_model = session.query(DataFlowModel).get(str(data_flow_id))
    component_model = session.query(ComponentModel).get(str(component_id))

    data_flow_model.end = component_model
    session.commit()

    return data_flow_model
