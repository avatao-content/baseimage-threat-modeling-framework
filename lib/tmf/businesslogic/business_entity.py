# Copyright (C) 2018 Avatao.com Innovative Learning Kft.
# All Rights Reserved. See LICENSE file for details.

from abc import ABC
from uuid import UUID

class BusinessEntity(ABC):
    def __init__(self, entity_id: UUID) -> None:
        self._id = entity_id

    @property
    def id(self):
        return self._id
