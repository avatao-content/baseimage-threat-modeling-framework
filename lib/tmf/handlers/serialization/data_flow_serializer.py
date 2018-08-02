# Copyright (C) 2018 Avatao.com Innovative Learning Kft.
# All Rights Reserved. See LICENSE file for details.

from tmf.handlers import domain_name
from .threat_serializer import ThreatSerializer
from .component_serializer import *


class DataFlowSerializer:

    def __init__(self, data_flow):
        self._data_flow = data_flow
        self._path = "/static/data_flows/"

    def create_full_dictionary(self):
        return {
            "id" : self._data_flow.id_,
            "name" : self._data_flow.name,
            "description" : self._data_flow.description,
            "system id" : self._data_flow.system_id,
            "type" : self._data_flow.type,
            "href" : domain_name + self._path + str(self._data_flow.id_),
            "threats" : [ThreatSerializer(threat).create_one_level_dictionary() for threat in self._component.threats],
            "start point" :  ComponentSerializer(data_flow_model.start_point).create_one_level_dictionary() if data_flow_model.start_point else "",
            "end point" :  ComponentSerializer(data_flow_model.end_point).create_one_level_dictionary() if data_flow_model.end_point else ""
        }

    def create_one_level_dictionary(self):
        return {
            "id" : self._data_flow.id_,
            "name" : self._data_flow.name,
            "description" : self._data_flow.description,
            "href" : domain_name + self._path + str(self._data_flow.id_)
        }
