from typing import Any

def verify_type(value: str) -> Any:
    return value if value is not None else 'NaN'

def apply_settings(reddit: object, sub: str, sort_by: str, limit: int=25):

    sort_options = ['hot', 'new', 'top']

    if sort_by not in sort_options:
        raise ValueError('Invalid Option')
    elif sort_by == 'hot':
        return reddit.subreddit(sub).hot(limit=limit)
    elif sort_by == 'top':
        return reddit.subreddit(sub).top(limit=limit)
    else:
        sort_by = 'new'
        return reddit.subreddit(sub).hot(limit=limit)


