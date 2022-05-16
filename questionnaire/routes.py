from flask import render_template, url_for, flash, redirect, request,session
from questionnaire.forms import SignupForm, LoginForm, QuestionsForm1, QuestionsForm2, QuestionsForm3, ForgotForm, NewpasswordForm
from passlib.hash import sha256_crypt
from MySQLdb import escape_string as thwart
from questionnaire.dbconnect import connection
from questionnaire.questionslist import questionslist
from functools import wraps
import gc
from questionnaire import app, s
from flask_mail import Mail, Message
from itsdangerous import SignatureExpired, BadTimeSignature
mail = Mail(app)

@app.route('/')
@app.route('/login', methods=['GET','POST'])
def Login():
	form = LoginForm()
	if form.validate_on_submit() and request.method == 'POST':
		c, conn = connection()
		data = c.execute("SELECT * FROM users WHERE email = %s", [thwart(form.email.data)])
		if data:
			data = c.fetchone()[2]

			if sha256_crypt.verify(form.password.data, data):
				session['logged_in'] = True
				uname = c.execute("SELECT * FROM users WHERE email = %s", [thwart(form.email.data)])
				uname = c.fetchone()[0]
				session['username'] = uname

				flash('you have been logged in!', 'success')
				return redirect(url_for('Welcome'))
			else:
				flash('please check credentials','danger')

		else:
			flash('please check credentials','danger')
		
		gc.collect()

	return render_template('loginpage.html', title = 'Login', form = form )


@app.route('/signup', methods=['GET','POST'])
def Signup():
	form = SignupForm()
	
	if form.validate_on_submit() and request.method == 'POST':
			username = form.username.data
			email = form.email.data
			password = sha256_crypt.encrypt(str(form.password.data))
			c, conn = connection()
			x = c.execute("SELECT * FROM users WHERE username = %s", [thwart(username)])
			
			if int(x) > 0:
				flash('username already taken!', 'danger')
				return redirect(url_for('Signup'))
			
			x = c.execute("SELECT * FROM users WHERE email = %s", [thwart(email)])
			
			if int(x) > 0:
				flash('user with this mail id is already registered please login!', 'danger')
				return redirect(url_for('Signup'))

			else:
				c.execute("INSERT INTO users (username, email, password) VALUES (%s, %s, %s)", 
				(thwart(username), thwart(email), thwart(password)))

				conn.commit()
				c.close()
				conn.close()

				gc.collect()

			flash(f'Account Created for { form.username.data }, please Login!', 'success')
			return redirect(url_for('Login'))
			
	return render_template('signuppage.html', title = 'Signup', form = form )


def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash("You need to login first",'danger')
            return redirect(url_for('Login'))

    return wrap


@app.route('/home')
@app.route('/welcome', methods=['GET','POST'])
@login_required
def Welcome():
	ql, questions = questionslist()
	c, conn = connection()
	usr = session['username']
	ans = c.execute("SELECT * FROM answers WHERE username = %s", [session['username']])
	if ans:
		ans = c.fetchone()[1:]
	else:
		flash("No data available, please fill the questionnaire below!",'success')
		return redirect(url_for('Questions1'))

	return render_template('welcome.html', title = 'Welcome', usr=usr, ans = ans, qns=questions, leng=ql)


@app.route('/q1', methods=['GET','POST'])
@login_required
def Questions1():
	form = QuestionsForm1()
	if form.validate_on_submit() and request.method == 'POST':
			c, conn = connection()
			q1 = form.q1.data
			q2 = form.q2.data
			q3 = form.q3.data
			q4 = form.q4.data
			q5 = form.q5.data
			uid = c.execute("SELECT * FROM users WHERE username = %s", [session['username']])
			uid = c.fetchone()[0]
			
			usr = c.execute("SELECT * FROM answers WHERE username = %s", [uid])
			if usr :
				c.execute(" UPDATE answers SET q1= %s, q2 = %s, q3 = %s, q4 = %s, q5 = %s WHERE username = %s ",
				(thwart(q1), thwart(q2), thwart(q3), thwart(q4), thwart(q5), thwart(uid)))

			else:
				c.execute("INSERT INTO answers (username, q1, q2, q3, q4, q5) VALUES (%s, %s, %s, %s, %s, %s)", 
				(thwart(uid), thwart(q1), thwart(q2), thwart(q3), thwart(q4), thwart(q5)))

			conn.commit()
			c.close()
			conn.close()

			gc.collect()
			return redirect(url_for('Questions2'))
	return render_template('questions1.html', title = 'SEIL', form = form)


@app.route('/q2', methods=['GET','POST'])
@login_required
def Questions2():
	form = QuestionsForm2()
	if form.validate_on_submit() and request.method == 'POST':
			c, conn = connection()
			q6 = form.q6.data
			q7 = form.q7.data
			q8 = form.q8.data
			q9 = form.q9.data
			q10 = form.q10.data
			uid = c.execute("SELECT * FROM users WHERE username = %s", [session['username']])
			uid = c.fetchone()[0]
			
			usr = c.execute("SELECT * FROM answers WHERE username = %s", [uid])
			if usr :
				c.execute(" UPDATE answers SET q6= %s, q7 = %s, q8 = %s, q9 = %s, q10 = %s WHERE username = %s ",
				(thwart(q6), thwart(q7), thwart(q8), thwart(q9), thwart(q10), thwart(uid)))

			else:
				c.execute("INSERT INTO answers (username, q6, q7, q8, q9, q10) VALUES (%s, %s, %s, %s, %s, %s)", 
				(thwart(uid), thwart(q6), thwart(q7), thwart(q8), thwart(q9), thwart(q10)))

			conn.commit()
			c.close()
			conn.close()

			gc.collect()
			return redirect(url_for('Questions3'))
	return render_template('questions2.html', title = 'SEIL', form = form)


@app.route('/q3', methods=['GET','POST'])
@login_required
def Questions3():
	form = QuestionsForm3()
	if form.validate_on_submit() and request.method == 'POST':
			c, conn = connection()
			q11 = form.q11.data
			q12 = form.q12.data
			q13 = form.q13.data
			q14 = form.q14.data
			q15 = form.q15.data
			uid = c.execute("SELECT * FROM users WHERE username = %s", [session['username']])
			uid = c.fetchone()[0]
			
			usr = c.execute("SELECT * FROM answers WHERE username = %s", [uid])
			if usr :
				c.execute(" UPDATE answers SET q11= %s, q12 = %s, q13 = %s, q14 = %s, q15 = %s WHERE username = %s ",
				(thwart(q11), thwart(q12), thwart(q13), thwart(q14), thwart(q15), thwart(uid)))

			else:
				c.execute("INSERT INTO answers (username, q1, q2, q3, q4, q5) VALUES (%s, %s, %s, %s, %s, %s)", 
				(thwart(uid), thwart(q11), thwart(q12), thwart(q13), thwart(q14), thwart(q15)))

			conn.commit()
			c.close()
			conn.close()

			gc.collect()
			return redirect(url_for('Welcome'))
	return render_template('questions3.html', title = 'SEIL', form = form)


@app.route("/logout/")
@login_required
def Logout():
    session.clear()
    flash("You have been logged out!",'success')
    gc.collect()
    return redirect(url_for('Login'))


@app.route('/forgotpassword', methods=['GET','POST'])
def Forgot():
	form = ForgotForm()
	email = form.email.data
	token = s.dumps(email, salt='email-confirm')

	if request.method == 'POST':
		msg = Message('Confirm Email', sender='seilwebapp@gmail.com', recipients=[email])
		link = url_for('Confirm_email', token= token, _external=True)
		msg.body = 'Use this link( {} ) to reset your password'.format(link)

		mail.send(msg)
		flash("An email with password reset link is sent. please check your inbox!",'success')
	return render_template('forgotpasswordpage.html', title = 'Forgot Password', form = form)


@app.route('/confirm_email/<token>', methods=['GET','POST'])
def Confirm_email(token):
	form = NewpasswordForm()

	if form.validate_on_submit() and request.method == 'POST':
		try:
			email = s.loads(token, salt='email-confirm', max_age=900)
		except SignatureExpired:
			return 'Link Expired'
		except BadTimeSignature:
			return 'Link not found'

		c, conn = connection()
		data = c.execute("SELECT * FROM users WHERE email = %s", [thwart(email)])
		if data:
			data = c.fetchone()[2]

			password = sha256_crypt.encrypt(str(form.new_password.data))

			c.execute(" UPDATE users SET password= %s", (thwart(password),))

			conn.commit()
			c.close()
			conn.close()

			gc.collect()

			flash("Password reset Successfully!",'success')
			return redirect(url_for('Login'))

	return render_template('newpassword.html', title = 'Forgot Password', form = form)