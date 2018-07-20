# Copyright (C) 2018 Avatao.com Innovative Learning Kft.
# All Rights Reserved. See LICENSE file for details.

from uuid import UUID


class NotInTheSameSystemError(Exception):

    def __init__(self, system_id_1 : UUID, system_id_2 : UUID, message = "are not the same system"):
        self.system_id_1 = system_id_1
        self.system_id_2 = system_id_2
        self.message = message

    def __str__(self):
        return self.system_id_1 + " " + self.system_id_2 + " " + self.message
