from flask_wtf import FlaskForm
from wtforms import IntegerField, SelectField, SubmitField, StringField
from wtforms.validators import DataRequired
from app.models import Course, db


class CourseForm(FlaskForm):
    coursename = StringField('Course', validators=[DataRequired()])
    shortname = StringField('ShortName', validators=[DataRequired()])
    submit_btn = SubmitField('Submit')

class TopicForm(FlaskForm):
    topic = StringField('Topic: ', validators=[DataRequired()])
    course_id = IntegerField('Course_id: ', validators=[DataRequired()])
    submit_btn = SubmitField('Submit')

class ScoreForm(FlaskForm):
    score_category = StringField('Score Category: ', validators=[DataRequired()])
    score_points = IntegerField('Score Points: ', validators=[DataRequired()])
    submit_btn = SubmitField('Submit')   

 
# class ReportForm(FlaskForm):
#     report_message = StringField('Report Message: ', validators=[DataRequired()])
#     report_date = IntegerField('Score Points: ', validators=[DataRequired()])
#     question_id = IntegerField('Question ID: ', validators=[DataRequired()])
#     user_id = IntegerField('User ID: ', validators=[DataRequired()])
#     submit_btn = SubmitField('Submit')   

class QuestionForm(FlaskForm) :
    questiona = StringField('Questiona : ', validators=[DataRequired()])
    option_a = StringField('Option_A: ', validators=[DataRequired()])
    option_b = StringField('Option_B: ', validators=[DataRequired()])
    option_c = StringField('Option_C: ', validators=[DataRequired()])
    option_d = StringField('Option_D: ', validators=[DataRequired()])
    answer = StringField('Answer: ', validators=[DataRequired()])
    course_id = IntegerField('Course ID: ', validators=[DataRequired()])
    # my_courses = [(c.shortname,c.coursename) for c in Course.query.all()]
    # course = SelectField('Course : ', choices = my_courses)
    topic_id = IntegerField('Topic ID: ')
    score_id = IntegerField('Score ID: ', validators=[DataRequired()])
    submit_btn = SubmitField('Submit')



    ######################################################################################################################

class QuestionaForm(FlaskForm) :
    questiona = StringField('Questiona :', validators=[DataRequired()])
    option_a = StringField('Option_A: ', validators=[DataRequired()])
    option_b = StringField('Option_B: ', validators=[DataRequired()])
    option_c = StringField('Option_C: ', validators=[DataRequired()])
    option_d = StringField('Option_D: ', validators=[DataRequired()])
    answer = StringField('Answer: ', validators=[DataRequired()])
  
    submit_btn = SubmitField('Submit')

class StudForm(FlaskForm):
    studname = StringField('name', validators=[DataRequired()])
    submit_btn=SubmitField('Submit')