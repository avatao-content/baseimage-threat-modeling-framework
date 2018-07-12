# Copyright (C) 2018 Avatao.com Innovative Learning Kft.
# All Rights Reserved. See LICENSE file for details.

from abc import ABC, abstractmethod

class Threat(ABC):
    def __init__(self):
        self._detected = False

    @abstractmethod
    def check_vulnarabilities(self, code_snippet):
        raise NotImplementedError

    def detect(self):
        self._detected = True

    def _readable_class_name(self):
        return Threat.convert_pascal_case_to_readable_format(type(self).__name__)

    def __str__(self):
        return ("Detected" if self._detected else "Undetected") + self._readable_class_name()

    @staticmethod
    def convert_pascal_case_to_readable_format(text):
        """ Converts a string written in Pascal case to a readable format,
        by making all uppercase characters lowercase and
        inserting a space before them.

        For example, "ClassNameInCamelCase" -> " class name in camel case"
        """
        return "".join(list(map(lambda x : " " + x.lower() if x.isupper() else x, list(text))))
