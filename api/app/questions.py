from flask import Flask,request
from flask_restful import Resource, Api


app = Flask(__name__)
api = Api(app)

aquestions=[]

class questions(Resource):
    def get(self):
        return {'id': 'questions'}

api.add_resource(questions, '/api/v1/users/questions/all', methods=['GET'])



class get_question_id(Resource):
    def get(self, question_id):
        return {question_id: aquestions[question_id]}

    def put(self, question_id):
        aquestions[question_id] = request.form['data']
        return {question_id: aquestions[question_id]}

api.add_resource(get_question_id, '/<questions:questions_id>')


class post_answers(Resource):


    def post(self, answer_id):
        return {answer_id: aquestions[answer_id]}

    def put(self, answer_id):
        aquestions[answer_id] = request.form['data']
        return {answer_id: aquestions[answer_id]}

api.add_resource(get_question_id, '/<questions:questions_id>')



if __name__ == '__main__':
    app.run(debug=True)


