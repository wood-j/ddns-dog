# -*- coding: utf-8 -*-
import json
from datetime import date
from datetime import datetime


class JsonSerializable(object):
    """ the base class for json serializable classes """

    def dumps(self):
        return json.dumps(self, indent=4, ensure_ascii=False, cls=DefaultEncoder)


class DefaultEncoder(json.JSONEncoder):
    """ the default encoder for object json serialize """
    def default(self, field):
        if isinstance(field, datetime):
            return field.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(field, date):
            return field.strftime('%Y-%m-%d')
        elif hasattr(field, '__dict__'):
            return field.__dict__
        else:
            return json.JSONEncoder.default(self, field)
