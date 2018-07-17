# Copyright (C) 2018 Avatao.com Innovative Learning Kft.
# All Rights Reserved. See LICENSE file for details.

from abc import ABC, abstractmethod
from uuid import UUID

from tmf.businesslogic import ThreatContainerMixin, BusinessEntity


class DataFlow(BusinessEntity, ThreatContainerMixin, ABC):
    """
    Abstract base class representing a data flow (link) between two components.
    """

    def __init__(self, entity_id : UUID, name : str = "Data flow", description : str = ""):
        super().__init__(entity_id)
        self._end_point = None
        self._start_point = None
        self._name = name
        self._description = description

    @abstractmethod
    def use(self):
        """
        Abstract method for specifying behavior of each data flows.
        """
        raise NotImplementedError

    def set_start_point(self, component):
        self._start_point = component

    def set_end_point(self, component):
        self._end_point = component

    def add_threat(self, threat):
        self._threats.append(threat)

    def remove_threat(self, threat):
        self._threats.remove(threat)

    def __str__(self):
        return self._name + ", start point: " + str(self._start_point) + ", end point: " + str(self._end_point)
