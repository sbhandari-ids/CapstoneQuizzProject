from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash


db = SQLAlchemy()

# user_question = db.Table(
#     'user_question'
# )

# class Quiz(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     date = db.Column (db.DateTime, default= datetime.utcnow())
#     total_score = db.Column(db.Integer, nullable=False)
#     user_score = db.Column(db.Integer, nullable=False)
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

#     def __init__(self, total_score, user_score, user_id):
#         self.total_score = total_score
#         self.user_score = user_score
#         self.user_id = user_id

#     def save(self):
#         db.session.add(self)
#         db.session.commit()
    



class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    # phonenumber = db.Column(db.String, nullable=False)
    # member_since = db.Column(db.DateTime, nullable=False)

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = generate_password_hash(password)
        # self.phonenumber = phonenumber
        # self.member_since = datetime.now()

    def save(self):
        db.session.add(self)
        db.session.commit()


  
   
class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    coursename = db.Column(db.String, unique=True, nullable=False)
    shortname = db.Column(db.String, unique = True, nullable = False)
    
    def __init__(self, coursename, shortname):
        self.coursename = coursename
        self.shortname = shortname

    def save(self):
        db.session.add(self)
        db.session.commit()
        

class Topic(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    topic = db.Column(db.String, unique=True, nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'), nullable=False)
    
    def __init__(self, topic, course_id ):
        self.topic = topic
        self.course_id = course_id
     
    def save(self):
        db.session.add(self)
        db.session.commit()


class Score(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    score_category = db.Column(db.String, unique=True, nullable=False)
    score_points = db.Column(db.Integer, unique=True, nullable=False)
    
    def __init__(self, score_category , score_points ):
        self.score_category = score_category
        self.score_points = score_points
     
    def save(self):
        db.session.add(self)
        db.session.commit()
       

class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    questiona = db.Column(db.String, nullable=False)
    option_a = db.Column(db.String, nullable=False)
    option_b = db.Column(db.String, nullable=False)
    option_c = db.Column(db.String, nullable=False)
    option_d = db.Column(db.String, nullable=False)
    answer = db.Column(db.String, nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'), nullable=False)
    topic_id = db.Column(db.Integer, db.ForeignKey('topic.id'))
    score_id = db.Column(db.Integer, db.ForeignKey('score.id'), nullable=False)

    def __init__(self, questiona, option_a, option_b, option_c, option_d, answer, course_id, topic_id, score_id ):
        self.questiona = questiona
        self.option_a = option_a
        self.option_b = option_b
        self.option_c = option_c
        self.option_d = option_d
        self.answer = answer
        self.course_id = course_id
        self.topic_id = topic_id
        self.score_id = score_id
     
    def save(self):
        db.session.add(self)
        db.session.commit()





# class Report(db.Model):
# #     id = db.Column(db.Integer, primary_key=True)
#     report_message = db.Column(db.String, unique=True, nullable=False)
#     report_date = db.Column (db.DateTime, default= datetime.utcnow())
#     question_id = db.Column(db.Integer, db.ForeignKey('question.id'))
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    

#     def __init__(self, report_message , question_id, user_id ):
#         self.report_message = report_message
#         # self.report_date = report_date
#         self.question_id = question_id
#         self.user_id = user_id
     
#     def save(self):
#         db.session.add(self)
#         db.session.commit()
        





        ###########################################################

class Questiona(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    questiona = db.Column(db.String, nullable=False)
    option_a = db.Column(db.String, nullable=False)
    option_b = db.Column(db.String, nullable=False)
    option_c = db.Column(db.String, nullable=False)
    option_d = db.Column(db.String, nullable=False)
    answer = db.Column(db.String, nullable=False)
   

    def __init__(self, questiona, option_a, option_b, option_c, option_d, answer):
        self.questiona = questiona
        self.option_a = option_a
        self.option_b = option_b
        self.option_c = option_c
        self.option_d = option_d
        self.answer = answer
      
     
    def save(self):
        db.session.add(self)
        db.session.commit()



class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    studname = db.Column(db.String, unique=True, nullable=False)
# phonenumber = db.Column(db.String, nullable=False)
# member_since = db.Column(db.DateTime, nullable=False)

    def __init__(self, studname):
        self.studname = studname
    # self.phonenumber = phonenumber
    # self.member_since = datetime.now()

    def save(self):
        db.session.add(self)
        db.session.commit()