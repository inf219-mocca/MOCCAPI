from time import gmtime

from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class Coffee(Resource):
    def get(self):
        return {
                "time": f"{gmtime()}",
                "coffee": {
                    "temperature": 1000,
                    "cups": 2,
                    "amount": 1
                    },
                "mocca": {
                    "isPowered": False,
                    "startedBrewing": "" + gmtime(),
                    "lostPower": True,
                    "outages": {
                        ["" + gmtime(), "" + gmtime()]
                        }
                    }
                }

api.add_resource(Coffee, '/v1/coffee')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5432, debug=True)
