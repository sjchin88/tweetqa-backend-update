from models import Prediction
from controllers import app
from .abstract.create_read_update_service import CreateReadUpdateService
import requests


class PredictionService(CreateReadUpdateService):
    ''' DataService, functions inherited from CreateReadUpdateService :
            read_by_id(id), create(entity_model), update(entity_model) '''

    def __init__(self):
        '''Constructor, take in the specific model class and pass the db.model back to the parent'''
        super().__init__(Prediction)

    def create(self, prediction: Prediction) -> Prediction:
        runner_ip = app.app.config['RUNNER_IP']
        dict_out = {"tweet": prediction.datum.tweet, "question": prediction.datum.question}
        res = requests.post('http://' + runner_ip + ':5555/', json=dict_out)
        dict_in = res.json()

        prediction.prediction = dict_in["answer"]
        saved_prediction = super().create(prediction)
        return saved_prediction

    def update(self, prediction: Prediction) -> Prediction:
        # TODO: Logic to be added to update the DATA collection
        saved_prediction = super().update(prediction)
        return saved_prediction
