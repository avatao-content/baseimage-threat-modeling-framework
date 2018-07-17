# Copyright (C) 2018 Avatao.com Innovative Learning Kft.
# All Rights Reserved. See LICENSE file for details.

from sqlalchemy import Column, String, Text
from sqlalchemy.orm import relationship

from .unit import UnitModel
from .generate_id import generate_id


class SystemModel(UnitModel):
    __tablename__ = 'systems'

    id_ = Column(String, primary_key = True, default = generate_id)
    name = Column(String)
    description = Column(Text)

    boundaries = relationship("BoundaryModel")
    data_flows = relationship("DataFlowModel")
