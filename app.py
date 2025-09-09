from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///attendance.db'
db = SQLAlchemy(app)

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))

class Attendance(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'))
    timestamp = db.Column(db.DateTime, default=datetime.datetime.utcnow)

@app.route('/mark_attendance', methods=['POST'])
def mark_attendance():
    data = request.json
    student_id = data.get('student_id')
    attendance = Attendance(student_id=student_id)
    db.session.add(attendance)
    db.session.commit()
    return jsonify({"message": "Attendance marked successfully!"})

if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)
