# Copyright (C) 2018 Avatao.com Innovative Learning Kft.
# All Rights Reserved. See LICENSE file for details.

from tmf.core import System
from tmf.core.boundaries import Boundary
from tmf.core.components import CodeComponent
from tmf.core.code import CodeSnippet
from tmf.core.data_flows import BinaryDataFlow
from tmf.core.data_flows import GenericDataFlow
from tmf.core.threats import DenialOfService

if __name__ == '__main__':

    system = System()
    code_component1 = CodeComponent([CodeSnippet("source1.cpp")])
    code_component2 = CodeComponent([CodeSnippet("source2.cpp")])
    system.global_boundary.add_component(code_component1)
    system.global_boundary.add_component(code_component2)
    binary_data_flow = BinaryDataFlow()

    generic_data_flow = GenericDataFlow()

    generic_data_flow.threats.append(DenialOfService())

    binary_data_flow.set_start_point(code_component1)
    binary_data_flow.set_end_point(code_component2)
    generic_data_flow.set_start_point(code_component2)
    generic_data_flow.set_end_point(code_component1)

    code_component1.add_inflow(generic_data_flow)
    code_component1.add_outflow(binary_data_flow)
    code_component2.add_inflow(binary_data_flow)
    code_component2.add_outflow(generic_data_flow)

    system.add_data_flow(binary_data_flow)
    system.add_data_flow(generic_data_flow)

    binary_data_flow.threats[0].detect()

    print(system.create_full_report())

    print(system.global_boundary.is_contained(CodeComponent()))

    code_component1.simulate([])

    code_component2.simulate([])
