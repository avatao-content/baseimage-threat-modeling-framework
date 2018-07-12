# Copyright (C) 2018 Avatao.com Innovative Learning Kft.
# All Rights Reserved. See LICENSE file for details.

from .component import Component

class CompositeComponent(Component):
    """
    Compenent that contains other components.
    Provides support for tree structure of components.
    """

    def __init__(self):
        super().__init__()
        self._children = []

    def add_component(self, component):
        self._children.append(component)

    def simulate(self, threats):
        for child in self._children:
            child.simulate(threats)
