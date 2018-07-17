# Copyright (C) 2018 Avatao.com Innovative Learning Kft.
# All Rights Reserved. See LICENSE file for details.

from tmf.businesslogic.threats import CustomThreat, DenialOfService, ElevationOfPrivilage, Tampering, InformationDisclosure, Repudiation, Spoofing


types = {
    "custom_threat" : CustomThreat,
    "denial_of_service" : DenialOfService,
    "elevation_of_privilage" : ElevationOfPrivilage,
    "information_disclosure" : InformationDisclosure,
    "repudiation" : Repudiation,
    "spoofing" : Spoofing,
    "tampering" : Tampering
}


def convert_threat_model_to_threat(threat_model):
    threat = types[threat_model.type]()

    threat._detected = threat_model.detected

    return threat
