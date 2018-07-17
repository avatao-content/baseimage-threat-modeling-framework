# Copyright (C) 2018 Avatao.com Innovative Learning Kft.
# All Rights Reserved. See LICENSE file for details.

from .data_flow import DataFlowModel


class GenericDataFlowModel(DataFlowModel):

    __mapper_args__ = {
        'polymorphic_identity':'generic_data_flow'
    }
