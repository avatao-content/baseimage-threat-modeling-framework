# Copyright (C) 2018 Avatao.com Innovative Learning Kft.
# All Rights Reserved. See LICENSE file for details.

from .data_flow import DataFlowModel


class BinaryDataFlowModel(DataFlowModel):

    __mapper_args__ = {
        'polymorphic_identity':'binary_data_flow'
    }
