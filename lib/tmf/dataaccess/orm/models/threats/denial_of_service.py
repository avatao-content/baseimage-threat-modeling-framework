# Copyright (C) 2018 Avatao.com Innovative Learning Kft.
# All Rights Reserved. See LICENSE file for details.

from .threat import ThreatModel


class DenialOfServiceModel(ThreatModel):

    __mapper_args__ = {
            'polymorphic_identity':'denial_of_service'
    }
