# Copyright (C) 2018 Avatao.com Innovative Learning Kft.
# All Rights Reserved. See LICENSE file for details.

from tmf.dataaccess.orm.models.data_flows import GenericDataFlowModel, CustomDataFlowModel, BinaryDataFlowModel
from tmf.dataaccess.orm.models.threats import CustomThreatModel, DenialOfServiceModel, ElevationOfPrivilageModel, InformationDisclosureModel, RepudiationModel, SpoofingModel, TamperingModel
from tmf.dataaccess.orm.models import BoundaryModel, ComponentModel, SystemModel, UnitModel, ThreatContainerModel
#TODO import component subclasses
from .session import engine

def init_db():
    """ Initializes the database, that is, creates all tables in it.
    """
    UnitModel.metadata.create_all(bind=engine)
