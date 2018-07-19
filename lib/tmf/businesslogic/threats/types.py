# Copyright (C) 2018 Avatao.com Innovative Learning Kft.
# All Rights Reserved. See LICENSE file for details.

from .custom_threat import CustomThreat
from .denial_of_service import DenialOfService
from .elevation_of_privilage import ElevationOfPrivilage
from .tampering import Tampering
from .information_disclosure import InformationDisclosure
from .repudiation import Repudiation
from .spoofing import Spoofing


types = {
    "custom_threat" : CustomThreat,
    "denial_of_service" : DenialOfService,
    "elevation_of_privilage" : ElevationOfPrivilage,
    "information_disclosure" : InformationDisclosure,
    "repudiation" : Repudiation,
    "spoofing" : Spoofing,
    "tampering" : Tampering
}
