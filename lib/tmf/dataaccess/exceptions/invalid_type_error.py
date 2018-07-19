# Copyright (C) 2018 Avatao.com Innovative Learning Kft.
# All Rights Reserved. See LICENSE file for details.


class InvalidTypeError(LookupError):

    def __init__(self, type : str, message = "type was not found"):
        self.type = type
        self.message = message

    def __str__(self):
        return self.type + " " + self.message
