# Copyright (C) 2018 Avatao.com Innovative Learning Kft.
# All Rights Reserved. See LICENSE file for details.

from .binary_data_flow import BinaryDataFlow
from .custom_data_flow import CustomDataFlow
from .generic_data_flow import GenericDataFlow


types = {
    "custom_data_flow" : CustomDataFlow,
    "generic_data_flow" : GenericDataFlow,
    "binary_data_flow" : BinaryDataFlow
}
