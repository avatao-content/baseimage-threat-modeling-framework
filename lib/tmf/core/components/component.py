# Copyright (C) 2018 Avatao.com Innovative Learning Kft.
# All Rights Reserved. See LICENSE file for details.

from abc import ABC, abstractmethod

from tmf.mixins import ThreatContainerMixin

class Component(ThreatContainerMixin, ABC):
    """
    Abstract base class representing a component of a system.
    """

    def __init__(self, name = "Component"):
        self._inflows = []
        self._outflows = []
        self._name = name
        super().__init__()

    @abstractmethod
    def simulate(self, threats):
        """
        Abstract method for simulating a component's behavior,
        in the presence of the specified threats.
        """
        raise NotImplementedError

    def add_outflow(self, data_flow):
        self._outflows.append(data_flow)

    def add_inflow(self, data_flow):
        self._inflows.append(data_flow)

    def remove_outflow(self, data_flow):
        self._outflows.remove(data_flow)

    def remove_inflow(self, data_flow):
        self._inflows.remove(data_flow)
