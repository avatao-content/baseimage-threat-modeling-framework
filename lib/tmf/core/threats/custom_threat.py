# Copyright (C) 2018 Avatao.com Innovative Learning Kft.
# All Rights Reserved. See LICENSE file for details.

from .threat import Threat

class CustomThreat(Threat):

    def check_vulnarabilities(self, code_snippet):
        pass
