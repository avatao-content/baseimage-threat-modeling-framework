# Copyright (C) 2018 Avatao.com Innovative Learning Kft.
# All Rights Reserved. See LICENSE file for details.

from sqlalchemy import Column, Boolean, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

from tmf.dataacces.orm.models import UnitModel


class ThreatModel(UnitModel):
    __tablename__ = 'threats'

    id_ = Column(String, primary_key = True, default = generate_id)
    detected = Column(Boolean)
    threat_container_id = Column(String, ForeignKey("threat_containers.id_"))
    type = Column(String)

    __mapper_args__ = {
            'polymorphic_on':type
    }
