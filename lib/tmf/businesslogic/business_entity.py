# Copyright (C) 2018 Avatao.com Innovative Learning Kft.
# All Rights Reserved. See LICENSE file for details.

from abc import ABC
from uuid import UUID

class BusinessEntity(ABC):
    def __init__(self, entity_id: UUID, name = "Businees Entity", description = "This is a business entity") -> None:
        self._id = entity_id
        self._name = name
        self._description = description

    @property
    def id(self):
        return self._id
