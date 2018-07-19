# Copyright (C) 2018 Avatao.com Innovative Learning Kft.
# All Rights Reserved. See LICENSE file for details.

from .binary_data_flow import BinaryDataFlowModel
from .custom_data_flow import CustomDataFlowModel
from .generic_data_flow import GenericDataFlowModel


types = {
    "custom_data_flow" : CustomDataFlowModel,
    "generic_data_flow" : GenericDataFlowModel,
    "binary_data_flow" : BinaryDataFlowModel
}