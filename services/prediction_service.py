from utils import tf_runner_best
from models import Prediction
from services.create_read_update_service import CreateReadUpdateService


class PredictionService(CreateReadUpdateService):
    ''' DataService, functions inherited from CreateReadUpdateService :
            read_by_id(id), create(entity_model), update(entity_model) '''

    def __init__(self):
        '''Constructor, take in the specific model class and pass the db.model back to the parent'''
        super().__init__(Prediction)

    def create(self, prediction: Prediction) -> Prediction:
        model_prediction = tf_runner_best.answer_tweet_question(prediction.datum.tweet, prediction.datum.question)
        prediction.prediction = model_prediction[0]
        saved_prediction = super().create(prediction)
        return saved_prediction

    def update(self, prediction: Prediction) -> Prediction:
        # TODO: Logic to be added to update the DATA collection
        saved_prediction = super().update(prediction)
        return saved_prediction
