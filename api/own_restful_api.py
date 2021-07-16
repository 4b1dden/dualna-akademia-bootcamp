from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

students = {
    0: {
        'meno': "fero",
        'trieda': "kvarta A"
    },
    1: {
        'meno': "jozo",
        'trieda': "sexta C"
    },
    2: {
        'meno': "matej",
        'trieda': "kvarta B"
    },
    3: {
        'meno': "aurelia",
        'trieda': "septima B"
    },
}

class DualnaAkademia(Resource):
    def get(self, student_id):
        if student_id not in students:
            return {
                'error': "User with given id does not exist."
            }

        return students[student_id]

    def put(self, student_id):
        name = request.form['name']
        _class = request.form['class']

        if name and _class:
            student = {
                'meno': name,
                'trieda': _class
            }
            students[student_id] = student

            return {
                'message': "Student created successfully",
                'data': student
            }

# curl http://localhost:5000/student/4 -d "name=test 123" -d "class=oktava a" -X PUT

api.add_resource(DualnaAkademia, '/student', '/student/<int:student_id>')

if __name__ == '__main__':
    app.run(debug=True)