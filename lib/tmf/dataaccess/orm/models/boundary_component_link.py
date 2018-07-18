# Copyright (C) 2018 Avatao.com Innovative Learning Kft.
# All Rights Reserved. See LICENSE file for details.

from sqlalchemy import Column, String, ForeignKey, Table

from .unit import UnitModel


boundary_component_link = Table("boundary-component", UnitModel.metadata,
                    Column("boundary_id", String, ForeignKey('boundaries.id_'), primary_key = True),
                    Column("component_id", String, ForeignKey('components.id_'), primary_key = True))
