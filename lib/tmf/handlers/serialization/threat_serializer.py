# Copyright (C) 2018 Avatao.com Innovative Learning Kft.
# All Rights Reserved. See LICENSE file for details.

from tmf.handlers import domain_name


class ThreatSerializer:

    def __init__(self, threat):
        self._threat = threat
        self._path = "/static/threats/"

    def create_full_dictionary(self):
        return {
            "id" : self._threat.id_,
            "name" : self._threat.name,
            "description" : self._threat.description,
            "type" : self._threat.type,
            "href" : domain_name + self._path + str(self._threat.id_),
            "detected" : self._threat.detected,
            "container" : self._threat.threat_container_id
        }

    def create_one_level_dictionary(self):
        return self.create_full_dictionary()
