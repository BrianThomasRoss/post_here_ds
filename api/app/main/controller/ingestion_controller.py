from flask import request
from flask_restplus import Resource

from ..util.ingestion_dto import IngestionDto
from ...ingestion import reddit_ingestor

api = IngestionDto.api
_instruct = IngestionDto.instruction

@api.route('/')
@api.param( 'begin','boolean, instruction to begin acquisition cycle')
@api.param('limit', 'number of posts to scrape per subreddit')
class Ingest(Resource):
    @api.doc('api triggered data ingestion')
    @api.expect(_instruct)
    def post(self):
        """event triggered ML pipeline"""
        data = request.json
        if data['begin']:
            cycle = reddit_ingestor.Scrape(limit=data['limit'])
            return {'status' : 'sucessful',
                    'ingestion': 'completed'}
        else:
            return {error}

