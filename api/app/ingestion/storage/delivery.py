from app.main import db
from .model import Post


class ProcessedPosts:

    def __init__(self):
        pass
    def already_saved(self, post: dict):
        return Post.query.filter_by(post_id=data['post_id']).first()

    def execute(self, data):
        try:
            db.session.add(data)
            db.session.commit()
        except Exception:
            pass

    def transfer(self, post: dict):
        """Converts dictionary of processed data to model class 
        used to execute SQL INSERT INTO statement"""

        if not self.already_saved(post):
            new_post = Post(post_id = data['post_id'],
                            subreddit = data['subreddit'],
                            created_utc = data['created_utc'],
                            created_local = data['created_local'],
                            title = data['title'],
                            author = data['author'],
                            body = data['body'],
                            num_comments = data['num_comments'],
                            score = data['score'],
                            up_ratio = data['up_ratio'],
                            nsfw  = data['nsfw'],
                            is_edited = data['is_edited'],
                            flair = data['flair'],
                            spoiler = data['spoiler'],
                            awards = data['awards'],
                            )
            return new_post
