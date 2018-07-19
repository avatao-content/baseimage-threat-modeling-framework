# Copyright (C) 2018 Avatao.com Innovative Learning Kft.
# All Rights Reserved. See LICENSE file for details.

from uuid import UUID

from tmf.dataaccess.orm.models import SystemModel, BoundaryModel, boundary_component_link
from .session import session
from .check_none import check_none
from .system import get_system_model_by_id
from .component import get_component_model_by_id


def get_boundary_model_by_id(id : UUID):
    boundary_model = session.query(BoundaryModel).get(str(id))
    check_none(boundary_model, id)

    return boundary_model

def create_new_boundary_model(system_id : UUID, name : str, description : str):
    boundary_model = BoundaryModel(name = name, description = description)

    system_model = get_system_model_by_id(system_id)
    system_model.boundaries.append(boundary_model)
    session.commit()

    return boundary_model

def set_boundary_name(id : UUID, name : str):
    boundary_model = get_boundary_model_by_id(id)
    boundary_model.name = name
    session.commit()

    return boundary_model

def set_boundary_description(id : UUID, description : str):
    boundary_model = get_boundary_model_by_id(id)
    boundary_model.description = description
    session.commit()

    return boundary_model

def add_component_to_boundary(boundary_id: UUID, component_id: UUID):
    boundary_model = get_boundary_model_by_id(boundary_id)
    component_model = get_component_model_by_id(component_id)

    boundary_model.components.append(component_model)
    session.commit()

    return session.query(boundary_component_link).get((str(boundary_id), str(component_id)))
