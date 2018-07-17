# Copyright (C) 2018 Avatao.com Innovative Learning Kft.
# All Rights Reserved. See LICENSE file for details.

from sqlalchemy import Column, String, ForeignKey, Table
from sqlalchemy.orm import relationship

from .unit import UnitModel
from .generate_id import generate_id


class ThreatContainerModel(UnitModel):
    __tablename__ = 'threat_containers'

    id_ = Column(String, primary_key = True, default = generate_id)
    type = Column(String)

    __mapper_args__ = {
        'polymorphic_on':type
    }

    threats = relationship("ThreatModel")
