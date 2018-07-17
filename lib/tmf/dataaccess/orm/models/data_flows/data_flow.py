# Copyright (C) 2018 Avatao.com Innovative Learning Kft.
# All Rights Reserved. See LICENSE file for details.

from sqlalchemy import Column, String, ForeignKey, Text
from sqlalchemy.orm import relationship

from tmf.dataaccess.orm.models import ThreatContainerModel


class DataFlowModel(ThreatContainerModel):
    __tablename__ = 'data_flows'

    id_ = Column(String, ForeignKey('threat_containers.id_'), primary_key = True)
    name = Column(String)
    description = Column(Text)
    type = Column(String)
    start_point_id = Column(String, ForeignKey("components.id_"))
    end_point_id = Column(String, ForeignKey("components.id_"))

    start_point = relationship("ComponentModel", back_populates = "outflows")
    end_point = relationship("ComponentModel", back_populates = "inflows")

    __mapper_args__ = {
        'polymorphic_on':type
    }
