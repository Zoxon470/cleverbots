from datetime import datetime


def datetime_convertor(obj):
    if isinstance(obj, datetime):
        return obj.__str__()
