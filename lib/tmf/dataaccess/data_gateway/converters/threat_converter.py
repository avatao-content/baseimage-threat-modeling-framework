# Copyright (C) 2018 Avatao.com Innovative Learning Kft.
# All Rights Reserved. See LICENSE file for details.

from tmf.businesslogic.threats import types


def convert_threat_model_to_threat(threat_model):
    threat = types[threat_model.type]()

    threat._detected = threat_model.detected

    return threat
