# Copyright (C) 2018 Avatao.com Innovative Learning Kft.
# All Rights Reserved. See LICENSE file for details.

from uuid import UUID

from tmf.businesslogic import System
from .boundary_converter import convert_boundary_model_to_boundary
from .data_flow_converter import convert_data_flow_model_to_data_flow


def convert_system_model_to_system(system_model):
    system = System(system_model.id_, name = system_model.name, description = system_model.description)

    for boundary in system_model.boundaries:
        system.add_boundary(convert_boundary_model_to_boundary(boundary))

    for data_flow in system_model.data_flows:
        system.add_boundary(convert_data_flow_model_to_data_flow(data_flow,system.global_boundary.components))

    return system
