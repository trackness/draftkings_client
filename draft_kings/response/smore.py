from desert import schema
from marshmallow import EXCLUDE, Schema


class Smore:
    _meta = {"unknown": EXCLUDE}

    @classmethod
    def schema(cls) -> Schema:
        return schema(cls, meta=cls._meta)

    @classmethod
    def load(cls, d: dict, **kwargs) -> 'Smore':
        return cls.schema().load(d, **kwargs)

    @classmethod
    def loads(cls, s: str, **kwargs) -> 'Smore':
        return cls.schema().loads(s, **kwargs)
