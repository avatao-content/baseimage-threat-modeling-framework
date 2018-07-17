# Copyright (C) 2018 Avatao.com Innovative Learning Kft.
# All Rights Reserved. See LICENSE file for details.

from tmf.businesslogic.components import Component
from .component_converter import convert_component_model_to_component


def convert_component_model_to_component(component_model):
    component = Component(entity_id = component_model.id_, name = component_model.name, description = component_model.description)

    #inflows and outflows will be inserted when creating the data flows

    return component
