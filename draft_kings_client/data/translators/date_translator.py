from datetime import datetime
import pytz


class DateTranslator:
    def __init__(self):
        pass

    @staticmethod
    def translate(date_string):
        return datetime.fromtimestamp(timestamp=long(date_string[6:-2]), tz=pytz.utc)