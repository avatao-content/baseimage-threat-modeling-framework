# Copyright (C) 2018 Avatao.com Innovative Learning Kft.
# All Rights Reserved. See LICENSE file for details.

from sqlalchemy import Column, String, ForeignKey, Table
from sqlalchemy.orm import relationship

from .unit import UnitModel
from .generate_id import generate_id


boundary_component_association_table = Table('boundary-component', UnitModel.metadata,
    Column('boundary_id', String, ForeignKey('boundaries.id_')),
    Column('component_id', String, ForeignKey('components.id_'))
)

class BoundaryModel(UnitModel):
    __tablename__ = 'boundaries'

    id_ = Column(String, primary_key = True, default = generate_id)
    system_id = Column(String, ForeignKey("systems.id_"))

    components = relationship("ComponentModel", secondary = boundary_component_association_table)
