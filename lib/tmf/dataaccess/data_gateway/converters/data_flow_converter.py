# Copyright (C) 2018 Avatao.com Innovative Learning Kft.
# All Rights Reserved. See LICENSE file for details.

from uuid import UUID

from tmf.businesslogic.data_flows import BinaryDataFlow, CustomDataFlow, GenericDataFlow


types = {
    "custom_data_flow" : CustomDataFlow,
    "generic_data_flow" : GenericDataFlow,
    "binary_data_flow" : BinaryDataFlow
}

def convert_data_flow_model_to_data_flow(data_flow_model, components):
    data_flow = types[threat_model.type](entity_id = data_flow_model.id_, name = data_flow_model.name, description = data_flow_model.description)

    _create_connections(data_flow, data_flow_model, components)

    return data_flow

def _create_connections(data_flow, data_flow_model, components):

    if data_flow_model.end_point is not None:
        end_point = next(component for component in components if component.id == UUID(data_flow_model.end_point.id))
        data_flow.set_end_point(end_point)
        end_point.add_inflow(data_flow)

    if data_flow_model.start_point is not None:
        start_point = next(component for component in components if component.id == UUID(data_flow_model.start_point.id))
        data_flow.set_start_point(start_point)
        start_point.add_outflow(data_flow)
