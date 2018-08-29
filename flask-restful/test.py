#coding:utf-8
from flask import Flask, request
from flask_restful import Resource, Api
from flask_restful import reqparse

app=Flask(__name__)
api=Api(app)

from flask_restful import fields, marshal_with

resource_fields = {
    'task':   fields.String,
    'uri':    fields.Url('todo_ep')
}

class TodoDao(object):
    def __init__(self, todo_id, task):
        self.todo_id = todo_id
        self.task = task

        # This field will not be sent in the response
        self.status = 'active'

class Todo(Resource):
    @marshal_with(resource_fields)
    def get(self, **kwargs):
        return TodoDao(todo_id='my_todo', task='Remember the milk')


class Todo1(Resource):
    def get(self,todo_id):
        # Default to 200 OK
        parser = reqparse.RequestParser()
        parser.add_argument('rate', type=int, help='Rate to charge for this resource')
        args = parser.parse_args()
        print todo_id
        return {'task': 'Hello world'}

class Todo2(Resource):
    def get(self):
        # Set the response code to 201
        return {'task': 'Hello world'}, 201

class Todo3(Resource):
    def get(self):
        # Set the response code to 201 and return custom headers
        return {'task': 'Hello world'}, 201, {'Etag': 'some-opaque-string'}

api.add_resource(Todo3,'/')
api.add_resource(Todo1,'/todo/<int:todo_id>', endpoint='todo_ep')






if __name__=="__main__":
    app.run(debug=True,port=5001)
