# Copyright (C) 2018 Avatao.com Innovative Learning Kft.
# All Rights Reserved. See LICENSE file for details.

from uuid import UUID

from tmf.dataaccess.orm.models import ComponentModel, BoundaryModel
from .session import session
from .check_none import check_none


def get_component_model_by_id(id : UUID):
    component_model = session.query(ComponentModel).get(str(id))
    check_none(component_model, id)

    return component_model

def create_new_component_model(boundary_id : UUID, name : str, description : str):
    component_model = ComponentModel(name = name, description = description)

    boundary_model = session.query(BoundaryModel).get(str(boundary_id))
    boundary_model.components.append(component_model)
    session.commit()

    return component_model

def set_component_name(id : UUID, name : str):
    boundary_model = session.query(ComponentModel).get(str(id))
    component_model.name = name
    session.commit()

    return component_model

def set_component_description(id : UUID, description : str):
    component_model = session.query(ComponentModel).get(str(id))
    component_model.description = description
    session.commit()

    return component_model
