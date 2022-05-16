from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField, RadioField, IntegerField
from wtforms.validators import DataRequired, Length, Email, EqualTo, Required

class SignupForm(FlaskForm):
	username = StringField('Userame', validators = [DataRequired(), Length(min=2, max=20)])
	email = StringField('Email', validators = [Email()])
	password = PasswordField('Password', validators = [DataRequired()])
	confirm_password = PasswordField('Confirm Password', validators = [DataRequired(), EqualTo('password')])
	submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
	email = StringField('Email', validators = [DataRequired(), Email()])
	password = PasswordField('Password', validators = [DataRequired()])
	remember = BooleanField('Remember Me')
	submit = SubmitField('Login')

class QuestionsForm1(FlaskForm):
	q1 = RadioField('This is a sample Question 1', choices=[('1','1'),('2','2'),('3','3'),('4','4'),('5','5')], validators=[Required()])
	q2 = RadioField('This is a sample Question 2', choices=[('1','1'),('2','2'),('3','3'),('4','4'),('5','5')], validators=[Required()])
	q3 = RadioField('This is a sample Question 3', choices=[('1','1'),('2','2'),('3','3'),('4','4'),('5','5')], validators=[Required()])
	q4 = RadioField('This is a sample Question 4', choices=[('1','1'),('2','2'),('3','3'),('4','4'),('5','5')], validators=[Required()])
	q5 = RadioField('This is a sample Question 5', choices=[('1','1'),('2','2'),('3','3'),('4','4'),('5','5')], validators=[Required()])
	submit = SubmitField('Submit')

class QuestionsForm2(FlaskForm):
	q6 = RadioField('This is a sample Question 6', choices=[('1','1'),('2','2'),('3','3'),('4','4'),('5','5')], validators=[Required()])
	q7 = RadioField('This is a sample Question 7', choices=[('1','1'),('2','2'),('3','3'),('4','4'),('5','5')], validators=[Required()])
	q8 = RadioField('This is a sample Question 8', choices=[('1','1'),('2','2'),('3','3'),('4','4'),('5','5')], validators=[Required()])
	q9 = RadioField('This is a sample Question 9', choices=[('1','1'),('2','2'),('3','3'),('4','4'),('5','5')], validators=[Required()])
	q10 = RadioField('This is a sample Question 10', choices=[('1','1'),('2','2'),('3','3'),('4','4'),('5','5')], validators=[Required()])
	submit = SubmitField('Submit')

class QuestionsForm3(FlaskForm):
	q11 = RadioField('This is a sample Question 11', choices=[('1','1'),('2','2'),('3','3'),('4','4'),('5','5')], validators=[Required()])
	q12 = RadioField('This is a sample Question 12', choices=[('1','1'),('2','2'),('3','3'),('4','4'),('5','5')], validators=[Required()])
	q13 = RadioField('This is a sample Question 13', choices=[('1','1'),('2','2'),('3','3'),('4','4'),('5','5')], validators=[Required()])
	q14 = RadioField('This is a sample Question 14', choices=[('1','1'),('2','2'),('3','3'),('4','4'),('5','5')], validators=[Required()])
	q15 = RadioField('This is a sample Question 15', choices=[('1','1'),('2','2'),('3','3'),('4','4'),('5','5')], validators=[Required()])
	submit = SubmitField('Submit')

class ForgotForm(FlaskForm):
	email = StringField('Email', validators = [DataRequired(), Email()])
	submit = SubmitField('Submit')

class NewpasswordForm(FlaskForm):
	new_password = PasswordField('New Password', validators = [DataRequired()])
	confirm_password = PasswordField('Confirm Password', validators = [DataRequired(), EqualTo('new_password')])
	submit = SubmitField('Submit')
