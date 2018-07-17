# Copyright (C) 2018 Avatao.com Innovative Learning Kft.
# All Rights Reserved. See LICENSE file for details.

from uuid import UUID

from .data_flow import DataFlow

class GenericDataFlow(DataFlow):

    def __init__(self, entity_id : UUID):
        super().__init__(entity_id)

    def use(self):
        """
        Abstract method for specifying behavior of each data flows.
        """
        self._end_point.simulate(self.threats)
