
from wtforms import SelectField
from . import admin 
from flask import Flask, flash, redirect, render_template, request,  url_for
from app.blueprints.admin.forms import CourseForm, QuestionForm, QuestionaForm, ScoreForm, StudForm, TopicForm
from app.models import Course, Question, Score, Student, Topic, db
from flask_login import login_required, current_user


@admin.route('/admin')#, methods = ['GET','POST'])
def adminHome():
    return render_template('admin_master.html')

@admin.route('/course', methods = ['GET','POST'])
def course():
   form = CourseForm()
   if request.method == 'POST' and form.validate_on_submit():
        coursename = form.coursename.data
        shortname = form.shortname.data
        new_course = Course(coursename, shortname)
        new_course.save()
        flash('Success ! New Course has been Added', 'success')
      #   return redirect(url_for('admin.course')) #login here is the function name for Login, not the route '/login'
        return render_template('admin.course')
   else:
      return render_template('course.html', form=form)
   

@admin.route('/topic', methods = ['GET','POST'])
def topic():
   form = TopicForm()
   if request.method == 'POST' and form.validate_on_submit():
        topic = form.topic.data
        course_id = form.course_id.data
        new_topic = Topic(topic, course_id)
        new_topic.save()
        flash('Success ! New Topic has been Added', 'success')
        return redirect(url_for('admin.topic')) #login here is the function name for Login, not the route '/login'
   else:
      return render_template('topic.html', form=form)
   
@admin.route('/score', methods = ['GET','POST'])
def score():
   form = ScoreForm()
   if request.method == 'POST' and form.validate_on_submit():
        score_category = form.score_category.data
        score_points = form.score_points.data
        new_score = Score(score_category, score_points)
        new_score.save()
        flash('Success ! New Topic has been Added', 'success')
        return redirect(url_for('admin.score')) #login here is the function name for Login, not the route '/login'
        #return render_template('admin_master.html')
   else:
      return render_template('score.html', form=form)
   
@admin.route('/question', methods = ['GET','POST'])
def question():
       form = QuestionForm()
       if request.method == 'POST': 
         questiona = form.questiona.data
         option_a = form.option_a.data
         option_b = form.option_b.data
         option_c = form.option_c.data
         option_d = form.option_d.data
         answer = form.answer.data
         course_id = form.course_id.data
         topic_id = form.topic_id.data
         score_id = form.score_id.data

         new_question=Question(questiona, option_a , option_b , option_c, option_d, answer, course_id, topic_id, score_id)
         #new_question=Question(question = question, option_a = option_a, option_b = option_b, option_c = option_c, option_d = option_d, answer = answer, course_id = course_id, topic_id = topic_id, score_id = score_id)

         new_question.save()
         my_courses = [(c.shortname,c.coursename) for c in Course.query.all()]
         course = SelectField('Course : ', choices = my_courses)
         print(my_courses)

         print(questiona)
         flash("Successfully created new question")
         return redirect(url_for('admin.question'))
       else: 
         return render_template('question.html', form=form)


@admin.route('/qfeed')
def qfeed():
   questions = Question.query.all()
   return render_template('qfeed.html', questions=questions)


@admin.route('/edit_question/<question_id>', methods =['GET', 'POST'])
def edit_question(question_id):
    question = Question.query.get(question_id)
    print(question)
    form = QuestionForm()
    if request.method == 'POST' and form.validate_on_submit():
        question.questiona = form.questiona.data
        question.option_a = form.option_a.data
        question.option_b = form.option_b.data
        question.option_c = form.option_c.data
        question.option_d = form.option_d.data
        question.answer = form.answer.data
        question.course_id = form.course_id.data
        question.topic_id = form.topic_id.data
        question.score_id = form.score_id.data

        question.save()
        flash('Question is Updated !')
        
        return redirect(url_for('admin.qfeed'))
    else :
        return render_template('edit_question.html', form=form, question=question)


    
@admin.route('/delete_question/<question_id>')
def delete_question(question_id):
    question = Question.query.get(question_id)
    print(question)
    
    db.session.delete(question)
    db.session.commit()
    flash(f'Question {question_id} Successfully Deleted', 'warning')
        
    return redirect(url_for('admin.qfeed'))
   

# @admin.route('/deletequestion/<question.id>')
# def deletequestion():
#     return redirect(url_for('admin.qfeed'))
    




#####################################################################################################################################################


@admin.route('/student', methods = ['GET','POST'])
def student():
    form = StudForm()
    if request.method == 'POST' and form.validate_on_submit():
        studname = form.studname.data
        new_stud = Student(studname)
        new_stud.save()
        flash("Successfully added Student",studname)
        return redirect(url_for('auth.login'))
    else:
        return render_template('student.html', form=form)




# @admin.route('/reportfeed')
# def reportfeed():
#    reports = Report.query.all()
#    return render_template('reportfeed.html', reports=reports)


@admin.route('/questiona', methods = ['GET','POST'])
def questiona():
       form = QuestionaForm()
       if request == 'POST': 
         questiona = form.questiona.data
         option_a = form.option_a.data
         option_b = form.option_b.data
         option_c = form.option_c.data
         option_d = form.option_d.data
         answer = form.answer.data
        #  course_id = form.course_id.data
        #  topic_id = form.topic_id.data
        #  score_id = form.score_id.data

         new_questiona=Question(questiona, option_a , option_b , option_c, option_d, answer)
         #new_question=Question(question = question, option_a = option_a, option_b = option_b, option_c = option_c, option_d = option_d, answer = answer, course_id = course_id, topic_id = topic_id, score_id = score_id)

         new_questiona.save()
         print(questiona)
         flash("Successfully created new question")
         return redirect(url_for('admin.questiona'))
       else: 
         return render_template('questiona.html', form=form)