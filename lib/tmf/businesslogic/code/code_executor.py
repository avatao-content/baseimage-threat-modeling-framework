# Copyright (C) 2018 Avatao.com Innovative Learning Kft.
# All Rights Reserved. See LICENSE file for details.

from abc import ABC, abstractmethod

class CodeExecutor(ABC):

    def __init__(self, file_path):
        self._file_path = file_path

    @abstractmethod
    def execute_code(self):
        raise NotImplementedError
