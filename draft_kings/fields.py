from datetime import datetime

from marshmallow.fields import AwareDateTime, DateTime, Field


class CustomAwareDateTime(AwareDateTime):
    def _deserialize(self, value, attr, data, **kwargs):
        """
        https://github.com/marshmallow-code/marshmallow/issues/656#issuecomment-318587611
        """
        if isinstance(value, datetime):
            if value.tzinfo is None:
                raise self.make_error(
                    "invalid", input=value, obj_type=self.OBJ_TYPE
                )
            return value
        return super()._deserialize(value, attr, data)

    def _serialize(self, value, attr, obj, **kwargs):
        if isinstance(value, datetime) and value.tzinfo is None:
            raise self.make_error("invalid", input=value, obj_type=self.OBJ_TYPE)
        return super()._serialize(value, attr, obj, **kwargs)


class CustomDateTime(DateTime):
    def _deserialize(self, value, attr, data, **kwargs):
        if isinstance(value, datetime):
            return value
        return super()._deserialize(value, attr, data)


class DictField(Field):
    """
    https://github.com/marshmallow-code/marshmallow/issues/120#issuecomment-81382070
    """

    def __init__(self, key_field, nested_field, *args, **kwargs):
        Field.__init__(self, *args, **kwargs)
        self.key_field = key_field
        self.nested_field = nested_field

    def _deserialize(self, value, attr, data, **kwargs):
        ret = {}
        for key, val in value.items():
            k = self.key_field.deserialize(key)
            v = self.nested_field.deserialize(val)
            ret[k] = v
        return ret

    def _serialize(self, value, attr, obj, **kwargs):
        ret = {}
        for key, _ in value.items():
            k = self.key_field._serialize(key, attr, obj)
            v = self.nested_field.serialize(key, self.get_value(attr, obj))
            ret[k] = v
        return ret
