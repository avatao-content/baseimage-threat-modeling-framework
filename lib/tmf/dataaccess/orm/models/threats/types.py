# Copyright (C) 2018 Avatao.com Innovative Learning Kft.
# All Rights Reserved. See LICENSE file for details.

from .custom_threat import CustomThreatModel
from .denial_of_service import DenialOfServiceModel
from .elevation_of_privilage import ElevationOfPrivilageModel
from .information_disclosure import InformationDisclosureModel
from .repudiation import RepudiationModel
from .spoofing import SpoofingModel
from .tampering import TamperingModel

types = {
    "custom_threat" : CustomThreatModel,
    "denial_of_service" : DenialOfServiceModel,
    "elevation_of_privilage" : ElevationOfPrivilageModel,
    "information_disclosure" : InformationDisclosureModel,
    "repudiation" : RepudiationModel,
    "spoofing" : SpoofingModel,
    "tampering" : TamperingModel
}