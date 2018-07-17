# Copyright (C) 2018 Avatao.com Innovative Learning Kft.
# All Rights Reserved. See LICENSE file for details.

from tmf.decorators import lazy_property

class ThreatContainerMixin:

    @lazy_property
    def threats(self):
        return []
