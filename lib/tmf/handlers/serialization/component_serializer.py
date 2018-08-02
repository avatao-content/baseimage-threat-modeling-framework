# Copyright (C) 2018 Avatao.com Innovative Learning Kft.
# All Rights Reserved. See LICENSE file for details.

from tmf.handlers import domain_name
from .threat_serializer import ThreatSerializer
from .data_flow_serializer import *


class ComponentSerializer:

    def __init__(self, component):
        self._component = component
        self._path = "/static/components/"

    def create_full_dictionary(self):
        return {
            "id" : self._component.id_,
            "name" : self._component.name,
            "description" : self._component.description,
            "href" : domain_name + self._path + str(self._component.id_),
            "threats" : [ThreatSerializer(threat).create_one_level_dictionary() for threat in self._component.threats],
            "inflows" : [DataFlowSerializer(inflow).create_one_level_dictionary() for inflow in self._component.inflows],
            "outflows" : [DataFlowSerializer(outflow).create_one_level_dictionary() for outflow in self._component.outflows],
        }

    def create_one_level_dictionary(self):
        return {
            "id" : self._component.id_,
            "name" : self._component.name,
            "description" : self._component.description,
            "href" : domain_name + self._path + str(self._component.id_)
        }
