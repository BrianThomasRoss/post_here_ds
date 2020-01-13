import string
import datetime as dt


def convert_time(timestamp: float) -> str:
    return dt.datetime.fromtimestamp(timestamp).strftime("%m-%d-%Y %H:%M:%S")

def process_text(text:str):
    """Scan for and remove selected characters and escape codes"""
    illegal = ['\r', '\n', '/', '  ', 'www', 'com']
    table = str.maketrans(string.punctuation, ' '*len(string.punctuation))

    for flag in flags:
        text = text.replace(flag, ' ')
    text = text.translate(table)

    return text

