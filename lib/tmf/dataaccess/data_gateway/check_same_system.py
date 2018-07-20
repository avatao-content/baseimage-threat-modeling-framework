# Copyright (C) 2018 Avatao.com Innovative Learning Kft.
# All Rights Reserved. See LICENSE file for details.

from uuid import UUID

from tmf.dataaccess.exceptions import NotInTheSameSystemError
from tmf.dataaccess.orm.models import SystemModel, BoundaryModel
from .session import session
from .check_none import check_none


def check_component_data_flow_in_same_system(component_model, data_flow_model, **kwargs):
    system_model = session.query(SystemModel).get(data_flow_model.system_id)
    check_none(system_model, data_flow_model.system_id)
    _check_component_in_system(system_model = system_model, component_model = component_model, **kwargs)

def check_component_boundary_in_same_system(component_model, boundary_model, **kwargs):
    system_model = session.query(SystemModel).get(boundary_model.system_id)
    check_none(system_model, boundary_model.system_id)
    _check_component_in_system(system_model = system_model, component_model = component_model, **kwargs)

def _check_component_in_system(system_model, component_model, **kwargs):
    for boundary in session.query(BoundaryModel).all():
        for component in boundary.components:
            if component.id_ == component_model.id_ and system_model.id_ != boundary.system_id:
                if("message" in kwargs):
                    raise NotInTheSameSystemError(boundary.system_id, system_model.id_, kwargs.get("message"))
                else:
                    raise NotInTheSameSystemError(boundary.system_id, system_model.id_)
