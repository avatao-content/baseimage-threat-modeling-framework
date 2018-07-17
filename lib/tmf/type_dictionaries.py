# Copyright (C) 2018 Avatao.com Innovative Learning Kft.
# All Rights Reserved. See LICENSE file for details.

from functools import partial

from composite_component import CompositeComponent
from code_component import CodeComponent

from binary_data_flow import BinaryDataFlow
from custom_data_flow import CustomDataFlow
from generic_data_flow import GenericDataFlow

components = {
    "cd" : CodeComponent,
    "cm" : CompositeComponent
}

data_flows = {
    "b" : BinaryDataFlow,
    "c" : CustomDataFlow,
    "g" : GenericDataFlow
}
