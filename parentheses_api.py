from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)

api = Api(app)

class parentheses(Resource):

    def get(self, str):
        open_list = ["[","{","("]
        close_list = ["]","}",")"]
        stack = []
        for i in str:
            if i in open_list:
                stack.append(i)
            elif i in close_list:
                pos = close_list.index(i)
                if ((len(stack) > 0) and
                    (open_list[pos] == stack[len(stack)-1])):
                    stack.pop()
                else:
                    data={"data": "Unbalanced"}
                    return data
        if len(stack) == 0:
            data={"data": "Balanced"}
            return data
        else:
            data={"data": "Unbalanced"}
            return data

api.add_resource(parentheses,'/parentheses/<string:str>')

if __name__=='__main__':
        app.run(debug=True, host="0.0.0.0", port=10002)

