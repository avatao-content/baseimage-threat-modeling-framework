# Copyright (C) 2018 Avatao.com Innovative Learning Kft.
# All Rights Reserved. See LICENSE file for details.

from tmf.dataaccess.orm.models.data_flows import GenericDataFlowModel, CustomDataFlowModel, BinaryDataFlowModel
from tmf.dataaccess.orm.models.threats import CustomThreatModel, DenialOfServiceModel, ElevationOfPrivilageModel, InformationDisclosureModel, RepudiationModel, SpoofingModel, TamperingModel
from tmf.dataaccess.orm.models import BoundaryModel, ComponentModel, boundary_component_link, SystemModel, UnitModel, ThreatContainerModel
#TODO import component subclasses
from tmf.dataaccess.data_gateway import engine

def init_db():
    """ Initializes the database by creating all tables in it."""
    UnitModel.metadata.create_all(bind=engine)

if __name__ == "__main__":
    init_db()
