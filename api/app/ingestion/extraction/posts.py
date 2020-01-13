import praw
from time import sleep
from typing import Union
from .utils import apply_settings, verify_type
from datetime import datetime as dt
from ..processing.services import process_text, convert_time
from ..storage.delivery import ProcessedPosts
from dotenv import load_dotenv
import os


# TODO: Fix text processing and convert_time functions

class Transcribe:
    """
    Parses a single post and returns the data received
    """
    text_fields = ['title', 'selftext']
    epoch_fields = ['created_utc', 'created']
    def __init__(self, post: object):
        self.post = post

    def retrieve(self, attribute: str) -> Union[str, int, float, bool]:
        return getattr(self.post, attribute)

    def absorb(self, features: dict, outbound: dict) -> dict:

        if not self.post.stickied:
            for key, value in features:
                if value in self.text_fields:
                    response = process_text(value)
                if value in self.epoch_fields:
                    response = convert_time(value)

                response = self.retrieve(value)
                outbound[key].append(verify_type(response))
                sleep(0.1)

class Retrieval:
    """
    Retrieves batch of posts from the Reddit API
    
    Args:
    -----
    subreddit: subreddit to collect from 
    limit: amount of post to retrieve
    sort_by: which category to sort posts by

    Returns:
    --------
    collection: dictionary of data
    """

    # praw object that interfaces with Reddit
    reddit = praw.Reddit(
                    client_id=os.getenv('client_id'),
                    client_secret=os.getenv('client_secret'),
                    user_agent=os.getenv('user_agent'))

    reddit.readonly = True

    # key-value pair of the DB model and attribute from where it is declared
    features = {'post_id':'id', 'subreddit':'subreddit_name_prefix',
    'post_title':'title', 'post_flair':'link_flair_text', 
    'submission_epoch_utc':'created_utc', 'submission_epoch_local':'created',
    'post_link':'shortlink', 'is_edited':'edited', 'is_nsfw':'over_18',
    'is_spoiler':'spoiler', 'post_score':'score', 'upvote_ratio':'upvote_ratio',
    'awards_received':'total_awards_received',
    'comments_received':'num_comments', 'post_text':'selftext',
    'image_url':'url'}

    # instantiate a dict to store the data collected from this batch
    subreddit_data = dict((key, []) for key in features.keys())

    def __init__(self, subreddit: str, limit: int = 10, sort_by: str = 'new'):

        self.sub = subreddit
        self.limit = limit
        self.sort_by = sort_by

    def connect(self) -> object:
        """Returns praw object initialized with the class params"""
        return apply_settings(self.reddit, self.sub, self.sort_by, self.limit)

    def collect_batch(self):
        """Retreives the batch of posts determined by the 
        class params"""
        posts = self.connect()

        for post in posts:
            Transcribe(post).absorb(self.features, collection)
            ProcessedPosts.execute(transfer(post))
