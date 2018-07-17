# Copyright (C) 2018 Avatao.com Innovative Learning Kft.
# All Rights Reserved. See LICENSE file for details.

from subprocess import Popen, PIPE

from .code_executor import CodeExecutor

class CppExecutor(CodeExecutor):

    def __init__(self, file_path):
        super().__init__(file_path)
        self._res_name = CppExecutor.replace_end_with(self._file_path,"o")


    def execute_code(self):
        self._compile_code()
        return self._run_code()

    def _compile_code(self):
        #g++ -Wall -Wextra -Werror -c main.cpp -o main.o
        compile_command = ['g++', '-Wall', '-Wextra', '-Werror', '-o', self._res_name, self._file_path ]
        process = Popen(compile_command, stdout = PIPE)
        out, err = process.communicate()
        if err is not None:
            raise RuntimeError

    def _run_code(self):
        #./main.out
        process = Popen([f'./{self._res_name}'], stdout = PIPE)
        out, err = process.communicate()
        if err is not None:
            raise RuntimeError
        return out

    @staticmethod
    def replace_end_with(text, replacement_text):
        """ Replaces the part of a string after the last period (.)
        with the specified text.

        For example, "www.website.com" -> "www.website.hu"
        """
        return text[:text.rindex(".")+1] + replacement_text
