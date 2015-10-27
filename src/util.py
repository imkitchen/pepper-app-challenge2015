#!/usr/bin/env python

import re

class Util:

    @staticmethod
    def to_snake_case(string):
        return re.sub("_(.)", lambda x:x.group(1).upper(), string)
        
    @staticmethod
    def to_camel_case(string):
        return re.sub("([A-Z])", lambda x:"_" + x.group(1).lower(), string)
