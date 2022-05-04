from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)

api = Api(app)

class square(Resource):
    def get(self, x):
        data={"data": x*x}
        return data
api.add_resource(square,'/square/<int:x>')

if __name__=='__main__':
        app.run(debug=True, host="0.0.0.0", port=10001)

