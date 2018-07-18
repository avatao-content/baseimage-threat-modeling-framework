# Copyright (C) 2018 Avatao.com Innovative Learning Kft.
# All Rights Reserved. See LICENSE file for details.

from sqlalchemy import Column, String, ForeignKey, Text
from sqlalchemy.orm import relationship

from .threat_container import ThreatContainerModel


class ComponentModel(ThreatContainerModel):
    __tablename__ = 'components'

    id_ = Column(String, ForeignKey('threat_containers.id_'), primary_key = True)
    name = Column(String)
    description = Column(Text)

    inflows = relationship("DataFlowModel", foreign_keys = "[DataFlowModel.end_point_id]", back_populates = "end_point")
    outflows = relationship("DataFlowModel", foreign_keys = "[DataFlowModel.start_point_id]", back_populates = "start_point")

    __mapper_args__ = {
        'polymorphic_identity':'component',
    }
