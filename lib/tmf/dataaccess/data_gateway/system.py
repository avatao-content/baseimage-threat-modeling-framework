# Copyright (C) 2018 Avatao.com Innovative Learning Kft.
# All Rights Reserved. See LICENSE file for details.

from uuid import UUID

from tmf.dataaccess.orm.models import SystemModel
from tmf.dataaccess.data_gateway.converters import convert_system_model_to_system
from .session import session


def get_system_by_id(id : UUID):
    system_model = session.query(SystemModel).get(str(id))

    system = convert_system_model_to_system(system_model)

    return system

def create_new_system_model(name, description):
    system_model = SystemModel(name = name, description = description)
    session.add(system_model)
    session.commit()

    return system_model

def set_system_name(id : UUID, name : str):
    system_model = session.query(SystemModel).get(str(id))
    system_model.name = name
    session.commit()

    return system_model

def set_system_description(id : UUID, description : str):
    system_model = session.query(SystemModel).get(str(id))
    system_model.description = description
    session.commit()

    return system_model
