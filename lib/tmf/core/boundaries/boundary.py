# Copyright (C) 2018 Avatao.com Innovative Learning Kft.
# All Rights Reserved. See LICENSE file for details.

class Boundary:

    def __init__(self):
        self._components = []

    def add_component(self, component):
        self._components.append(component)

    def remove_component(self, component):
        self._components.remove(component)

    def remove_component_at(self, index):
        self._components.pop(index)

    def is_contained(self, component):
        return component in self._components

    @property
    def components(self):
        return self._components

    def __str__(self):
        return "Boundary, contained components: " + ",".join(map(str,self._components))
