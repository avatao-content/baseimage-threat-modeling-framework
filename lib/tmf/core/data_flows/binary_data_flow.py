# Copyright (C) 2018 Avatao.com Innovative Learning Kft.
# All Rights Reserved. See LICENSE file for details.

from .data_flow import DataFlow
from tmf.core.threats import Tampering

class BinaryDataFlow(DataFlow):
    """
    Represents a binary data flow.
    """
    def __init__(self):
        super().__init__("Binary data flow")
        self.threats.append(Tampering())

    def use(self):
        """
        Abstract method for specifying behavior of each data flows.
        """
        self._end_point.simulate(self.threats)
