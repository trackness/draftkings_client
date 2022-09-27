from typing import Type

from desert import schema
from marshmallow import EXCLUDE, Schema
from marshmallow.fields import Nested, List, Str

from draft_kings.response.fields import DictField


class Smore:
    _meta = {"unknown": EXCLUDE}

    @classmethod
    def _schema(cls, _type: Type) -> Schema:
        return schema(_type, meta=cls._meta)

    @classmethod
    def nest(cls, nested_type: Type, **kwargs) -> Nested:
        return Nested(cls._schema(nested_type), **kwargs)

    @classmethod
    def list_nest(cls, nested_type: Type, **kwargs) -> List:
        return List(Nested(cls._schema(nested_type)), **kwargs)

    @classmethod
    def dict_nest(cls, nested_type: Type, **kwargs) -> DictField:
        return DictField(Str(required=True), Smore.nest(nested_type, required=True), **kwargs)

    @classmethod
    def load(cls, d: dict, **kwargs) -> 'Smore':
        return cls._schema(cls).load(d, **kwargs)

    @classmethod
    def loads(cls, s: str, **kwargs) -> 'Smore':
        return cls._schema(cls).loads(s, **kwargs)
