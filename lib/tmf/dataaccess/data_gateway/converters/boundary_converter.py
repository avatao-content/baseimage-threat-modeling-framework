# Copyright (C) 2018 Avatao.com Innovative Learning Kft.
# All Rights Reserved. See LICENSE file for details.

from tmf.businesslogic.boundaries import Boundary
from .component_converter import convert_component_model_to_component


def convert_boundary_model_to_boundary(boundary_model):
    boundary = Boundary(boundary_model.id_, name = boundary_model.name, description = boundary_model.description)

    for component in boundary_model.components:
        boundary.add_component(convert_component_model_to_component(component))

    return boundary
