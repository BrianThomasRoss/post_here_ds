import string
import datetime as dt


def convert_time(timestamp: float) -> str:
    return dt.datetime.fromtimestamp(timestamp).strftime("%m-%d-%Y %H:%M:%S")


