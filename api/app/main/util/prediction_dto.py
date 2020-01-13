from flask_restplus import Namespace, fields

class PredictionDto:
    api = Namespace('predict', description='prediction related operations')
    preds = api.model('Submission', {
        'return_count': fields.Integer(required=True,
             description='numbers of predictions to return'),
        'submission_text': fields.String(required=True,
             description='body of the post being used to make prediction')
    })