from ham.dxcc import DxccAll, dxobj
import logging

"""
This is an API Class so I can try and speed up Node-Red data processing.

"""


from flask import Flask
from flask_restx import Resource, Api

app = Flask(__name__)
api = Api(app)
dx=DxccAll()

@api.route('/hello')
class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}


@api.route('/call/<string:call>')
class CallLookup(Resource):
    def get(self,call):
        global dx
        return dx.find(call)

if __name__ == '__main__':
    app.run(debug=True)
