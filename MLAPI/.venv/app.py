from flask import Flask, request
from flask_restful import Api, Resource
import pickle
import pandas as pd
from flask_cors import CORS

app = Flask(__name__)

CORS(app)

api = Api(app)

class prediction(Resource):
    def get(self,budget):
        budget = [int(budget)]
        df = pd.DataFrame(budget, columns=['Marketing Budget (X) in Thousands'])
        model = pickle.load(open(r"C:\Users\JISHAN AICH\PycharmProjects\MLAPI\.venv\simple_linear_regression.pkl", 'rb'))
        prediction = model.predict(df)
        prediction = int(prediction[0])
        return str(prediction)

class getData(Resource):
    def get(self):
        df = pd.read_excel(r"C:\Users\JISHAN AICH\PycharmProjects\MLAPI\.venv\data.xlsx")
        df = df.rename({'Marketing Budget (X) in Thousands': 'budget', 'Actual Sales': 'sale'}, axis=1)
        res = df.to_json(orient='records')
        return res

api.add_resource(getData, '/api')
api.add_resource(prediction, '/prediction/<int:budget>')

if __name__ == '__main__':
    app.run(debug=True)