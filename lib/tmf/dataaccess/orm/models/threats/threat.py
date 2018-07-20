# Copyright (C) 2018 Avatao.com Innovative Learning Kft.
# All Rights Reserved. See LICENSE file for details.

from sqlalchemy import Column, Boolean, String, ForeignKey, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

from tmf.dataaccess.orm.models import UnitModel, generate_id


class ThreatModel(UnitModel):
    __tablename__ = 'threats'

    id_ = Column(String, primary_key = True, default = generate_id)
    name = Column(String)
    description = Column(Text)
    detected = Column(Boolean)
    threat_container_id = Column(String, ForeignKey("threat_containers.id_"), nullable = False)
    type = Column(String)

    __mapper_args__ = {
            'polymorphic_on':type
    }
