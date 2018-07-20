# Copyright (C) 2018 Avatao.com Innovative Learning Kft.
# All Rights Reserved. See LICENSE file for details.

from uuid import UUID

from sqlalchemy import and_

from tmf.dataaccess.orm.models import ComponentModel, BoundaryModel, boundary_component_link
from .session import session
from .boundary import get_boundary_model_by_id
from .check_none import check_none
from .check_same_system import check_component_boundary_in_same_system


def get_component_model_by_id(id : UUID):
    component_model = session.query(ComponentModel).get(str(id))
    check_none(component_model, id)

    return component_model

def create_new_component_model(boundary_id : UUID, name : str, description : str):
    component_model = ComponentModel(name = name, description = description)

    boundary_model = get_boundary_model_by_id(boundary_id)
    boundary_model.components.append(component_model)
    session.commit()

    return component_model

def set_component_name(id : UUID, name : str):
    component_model = get_component_model_by_id(id)
    component_model.name = name
    session.commit()

    return component_model

def set_component_description(id : UUID, description : str):
    component_model = get_component_model_by_id(id)
    component_model.description = description
    session.commit()

    return component_model

def add_component_to_boundary(boundary_id: UUID, component_id: UUID):
    boundary_model = get_boundary_model_by_id(boundary_id)
    component_model = get_component_model_by_id(component_id)
    check_component_boundary_in_same_system(boundary_model = boundary_model, component_model = component_model)

    boundary_model.components.append(component_model)
    session.commit()

    return session.execute(boundary_component_link.select().where( and_(
        boundary_component_link.columns.boundary_id == str(boundary_id),
        boundary_component_link.columns.component_id == str(component_id)))).fetchone()
