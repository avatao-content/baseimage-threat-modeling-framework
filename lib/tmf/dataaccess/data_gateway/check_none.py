# Copyright (C) 2018 Avatao.com Innovative Learning Kft.
# All Rights Reserved. See LICENSE file for details.

from uuid import UUID

from tmf.dataaccess.exceptions import InvalidPrimaryKeyError


def check_none(object, id : UUID, **kwargs):
    if(object is None):
        if("message" in kwargs):
            raise InvalidPrimaryKeyError(id, kwargs.get("message"))
        else:
            raise InvalidPrimaryKeyError(id)
