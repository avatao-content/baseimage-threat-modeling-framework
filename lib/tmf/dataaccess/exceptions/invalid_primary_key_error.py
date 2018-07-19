# Copyright (C) 2018 Avatao.com Innovative Learning Kft.
# All Rights Reserved. See LICENSE file for details.

from uuid import UUID


class InvalidPrimaryKeyError(LookupError):

    def __init__(self, key : UUID, message = " primary key was not found"):
        self.key = key
        self.message = message

    def __str__(self):
        return self.key + " " + self.message
