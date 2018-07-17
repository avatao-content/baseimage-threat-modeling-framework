# Copyright (C) 2018 Avatao.com Innovative Learning Kft.
# All Rights Reserved. See LICENSE file for details.

from abc import ABC, abstractmethod
from uuid import UUID

from tmf.businesslogic import ThreatContainerMixin, BusinessEntity


class Component(BusinessEntity, ThreatContainerMixin, ABC):
    """
    Abstract base class representing a component of a system.
    """

    def __init__(self, entity_id : UUID, name = "Component", description = ""):
        super().__init__(entity_id)
        self._inflows = []
        self._outflows = []
        self._name = name
        self._description = description

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
