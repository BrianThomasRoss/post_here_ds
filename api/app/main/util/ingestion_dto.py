from flask_restplus import Namespace, fields

class IngestionDto:
    api = Namespace('ingest', description='data acquisition')
    instruction = api.model('Ingestion', {
        'begin': fields.Boolean(required=True, description='begin acquisition'),
        'limit': fields.String(required=True, description='posts per subreddit')
    })