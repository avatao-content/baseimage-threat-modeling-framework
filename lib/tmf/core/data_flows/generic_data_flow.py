# Copyright (C) 2018 Avatao.com Innovative Learning Kft.
# All Rights Reserved. See LICENSE file for details.

from .data_flow import DataFlow

class GenericDataFlow(DataFlow):

    def use(self):
        """
        Abstract method for specifying behavior of each data flows.
        """
        self._end_point.simulate(self.threats)
