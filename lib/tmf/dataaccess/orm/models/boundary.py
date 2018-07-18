# Copyright (C) 2018 Avatao.com Innovative Learning Kft.
# All Rights Reserved. See LICENSE file for details.

from sqlalchemy import Column, String, ForeignKey, Text
from sqlalchemy.orm import relationship

from .unit import UnitModel
from .generate_id import generate_id
from .boundary_component_link import boundary_component_link


class BoundaryModel(UnitModel):
    __tablename__ = 'boundaries'

    id_ = Column(String, primary_key = True, default = generate_id)
    name = Column(String)
    description = Column(Text)
    system_id = Column(String, ForeignKey("systems.id_"))

    components = relationship("ComponentModel", secondary = boundary_component_link)
