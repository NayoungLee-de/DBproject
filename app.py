from flask import (Flask, render_template, request ,session,redirect,url_for)
import sqlite3

app = Flask(__name__)

@app.route('/')
def main():
	return render_template('main.html')

@app.route('/login')
def login():
	return render_template('login.html')

@app.route('/login_proc',methods=['POST'])
def login_proc():
	userId = request.form['id']
	userPw = request.form['pw']

	if len(userId) == 0 or len(userPw) == 0:
		return userId + ', ' + userPw + ' Login Data Not Found.'
	else:
		db = sqlite3.connect('data.db')
		cursor = db.cursor()
		sql = "select mNum, userId, userPw from member where userId = ? "
		cursor.execute(sql, (userId,))
		rows = cursor.fetchall()
		for rs in rows:
			print (rs)
			if userId == rs[1] and userPw == rs[2]:
				session['logFlag'] = True
				session['mNum'] = rs[0]
				session['userId'] = userId
					
				return redirect(url_for('main'))
			else:
				return redirect(url_for('login'))

@app.route('/logout')
def logout():
	session.clear()
	return redirect(url_for('main'))

app.secret_key = 'sample_secret_key'



if __name__ == '__main__':
	app.debug = True
	app.run(host = '127.0.0.1',port=5000)