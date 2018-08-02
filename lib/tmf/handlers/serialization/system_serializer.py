# Copyright (C) 2018 Avatao.com Innovative Learning Kft.
# All Rights Reserved. See LICENSE file for details.

from .boundary_serializer import BoundarySerializer
from tmf.handlers import domain_name


class SystemSerializer:

    def __init__(self, system):
        self._system = system
        self._path = "/static/systems/"

    def create_full_dictionary(self):
        return {
            "id" : self._system.id_,
            "name" : self._system.name,
            "description" : self._system.description,
            "href" : domain_name + self._path + str(self._system.id_),
            "boundaries" : [BoundarySerializer(boundary).create_one_level_dictionary() for boundary in self._system.boundaries],
            "data_flows" : [data_flow.id_ for data_flow in self._system.data_flows]
        }
