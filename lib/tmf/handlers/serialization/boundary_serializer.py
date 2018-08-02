# Copyright (C) 2018 Avatao.com Innovative Learning Kft.
# All Rights Reserved. See LICENSE file for details.

from tmf.handlers import domain_name
from .component_serializer import ComponentSerializer


class BoundarySerializer:

    def __init__(self, boundary):
        self._boundary = boundary
        self._path = "/static/boundaries/"

    def create_full_dictionary(self):
        return {
            "id" : self._boundary.id_,
            "name" : self._boundary.name,
            "description" : self._boundary.description,
            "href" : domain_name + self._path + str(self._boundary.id_),
            "system id" : self._boundary.system_id,
            "components" : [ComponentSerializer(component).create_one_level_dictionary() for component in self._boundary.components]
        }

    def create_one_level_dictionary(self):
        return {
            "id" : self._boundary.id_,
            "name" : self._boundary.name,
            "description" : self._boundary.description,
            "href" : domain_name + self._path + str(self._boundary.id_),
            "system id" : self._boundary.system_id
        }
