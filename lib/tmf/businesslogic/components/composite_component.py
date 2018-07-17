# Copyright (C) 2018 Avatao.com Innovative Learning Kft.
# All Rights Reserved. See LICENSE file for details.

from uuid import UUID

from .component import Component


class CompositeComponent(Component):
    """
    Compenent that contains other components.
    Provides support for tree structure of components.
    """

    def __init__(self, entity_id : UUID, name = "Composite component"):
        super().__init__(entity_id, name)
        self._children = []

    def add_component(self, component):
        self._children.append(component)

    def simulate(self, threats):
        for child in self._children:
            child.simulate(threats)
