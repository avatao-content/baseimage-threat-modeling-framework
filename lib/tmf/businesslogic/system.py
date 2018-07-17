# Copyright (C) 2018 Avatao.com Innovative Learning Kft.
# All Rights Reserved. See LICENSE file for details.

from uuid import UUID

from jsonpickle import encode, set_encoder_options

from tmf.core.boundaries import Boundary
from .business_entity import BusinessEntity


class System(BusinessEntity):
    """ Class representing a system.
    Contains all components and data flows in it.
    """
    def __init__(self, entity_id : UUID, name : str, description : str) -> None:
        super().__init__(entity_id)
        self._name = name
        self._description = description
        self._boundaries = [Boundary()] #TODO this is not needed if its retrieved from database
        self._data_flows = []

    def create_threat_report(self):
        """ Creates a list of all threats currently in the system.
        """
        return self._list_to_text(self._list_of_threats)

    def create_full_report(self):
        """ Creates a list of all elements currently in the system.
        This includes components, data flows, boundaries and threats.
        """
        set_encoder_options('json', sort_keys = True, indent = 4)

        return (f"Boundaries:\n{encode(self._boundaries)}\n"
                f"Components:\n{encode(self.global_boundary.components)}\n"
                f"Data flows:\n{encode(self._data_flows)}\n"
                f"Threats:\n{encode(self._list_of_threats())}\n")

        """return (f"Boundaries:\n{self._list_to_text(self._boundaries)}\n"
                f"Components:\n{self._list_to_text(self.global_boundary.components)}\n"
                f"Data flows:\n{self._list_to_text(self._data_flows)}\n"
                f"Threats:\n{self._list_to_text(self._list_of_threats())}\n")"""

    def _list_of_threats(self):
        return [threat for sub in (df.threats for df in list(set(self._data_flows).union(self._components))) for threat in sub]

    def _list_to_text(self, items):
        res = ''
        for item in items:
            res += str(item) + '\n'
        return res[:-1]


    def add_boundary(self, boundary):
        self._boundaries.append(boundary)

    def remove_boundary(self, boundary):
        self._boundaries.remove(boundary)

    def remove_boundary_at(self, index):
        self._boundaries.pop(index)

    def add_data_flow(self, data_flow):
        self._data_flows.append(data_flow)

    def remove_data_flow(self, data_flow):
        self._data_flows.remove(data_flow)

    def remove_data_flow_at(self, index):
        self._data_flows.pop(index)

    @property
    def data_flows(self):
        return self._data_flows

    @property
    def boundaries(self):
        return self._boundaries

    @property
    def global_boundary(self):
        return self._boundaries[0]
