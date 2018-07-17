# Copyright (C) 2018 Avatao.com Innovative Learning Kft.
# All Rights Reserved. See LICENSE file for details.

from os.path import splitext
from uuid import UUID

from tmf.businesslogic import BusinessEntity
from .cpp_executor import CppExecutor

class CodeSnippet(BusinessEntity):
    """
    Represents a code snippet. Can be executed by the simulate method.
    """

    _source_executors = {
        ".cpp" : CppExecutor
    }

    def __init__(self, entity_id : UUID, file_path):
        super().__init__(entity_id)
        self._file_path = file_path
        extension = splitext(file_path)[1]
        self._source_executor = self._create_source_executor(extension)

    def simulate(self, threats):
        print(self._source_executor.execute_code())

    def _create_source_executor(self, extension):
        return self._source_executors[extension](self._file_path)
