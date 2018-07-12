# Copyright (C) 2018 Avatao.com Innovative Learning Kft.
# All Rights Reserved. See LICENSE file for details.

from .component import Component
from tmf.core.code import CodeSnippet

class CodeComponent(Component):

    def __init__(self, code_snippets = [], name = "Code component"):
        super().__init__(name)
        self._code_snippets = code_snippets

    def simulate(self, threats):
        for code_snippet in self._code_snippets:
            code_snippet.simulate(threats)

    def add_code_snippet(self, code_snippet):
        self._code_snippets.append(code_snippet)

    def __str__(self):
        return f"{self._name} , contained code snippets: {','.join(map(str,self._code_snippets))}"
