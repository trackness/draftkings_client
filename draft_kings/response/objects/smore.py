from dataclasses import field

from desert import metadata
from desert import schema
from marshmallow import EXCLUDE
from marshmallow.fields import Field


class Smore:
    _meta = {"unknown": EXCLUDE}

    @classmethod
    def load(cls, d: dict, **kwargs):
        return schema(cls, meta=cls._meta).load(d, **kwargs)

    @classmethod
    def loads(cls, s: str, **kwargs):
        return schema(cls, meta=cls._meta).loads(s, **kwargs)

    @classmethod
    def field(cls, f: Field):
        return field(metadata=metadata(f))
