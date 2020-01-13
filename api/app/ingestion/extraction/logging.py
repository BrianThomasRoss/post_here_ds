from typing import BinaryIO
from datetime import datetime as dt
import joblib

class ExtractionMonitor:
    """
    Monitors and logs information concerning the Data Acquisition process.
    """

    date = dt.now().strftime("%m-%d-%Y")
    report = {f'ExtractionLog : {date}':{'errors':[], 'count': [],
            'duration':[]}}
    errors = {'error':[], 'occured_in':[]}
    date = dt.now().strftime("%m-%d-%Y")

    def __init__(self):
        pass

    def begin(self) -> float:
        return dt.utcnow()

    def log_error(self, ex: str, source: str):
        """
        log error
        """
        self.errors['error'].append(ex)
        self.errors['occured_in'].append(source)

    def tally(self, collection: dict) -> int:
        self.report['count'].append(dict(len(collection['post_id'])))

    def finalize(self, start: float) -> BinaryIO:

        wall = dt.utcnow() - start
        elapsed = f'{wall/60:.0f}:{wall%60:.0f}'
        self.report['duration'].append(elapsed)

        joblib.dump(self.report, f'{self.date}-extraction-log.joblib')

