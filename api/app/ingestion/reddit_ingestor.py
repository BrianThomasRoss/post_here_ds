from .extraction import posts, logging
from .storage.delivery import ProcessedPosts


class Scrape:

    subreddits = ['askreddit', 'askscience', 'datascience', 'jokes', 
    'learnpython', 'worldnews', 'amitheasshole', 'tifu', 'lifeprotips',
    'relationshipadvice', 'unpopularopinion', 'nostupidquestions', 'science',
    'legaladvice', 'personalfinance', 'outoftheloop']

    def __init__(self, limit: int):
        
        self.limit = limit

    def commence(self):

        Monitor = logging.ExtractionMonitor()
        start = Monitor.begin()

        for sub in self.subreddits:
            try:
                collection = posts.Retrieval.collect_batch(sub, 
                                                            limit=self.limit)

            except Exception as ex:
                Monitor.log_error(ex, sub)



