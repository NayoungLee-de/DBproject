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
		sql = "select mNum, userId, userPw from member where userId = ?"
		cursor.execute(sql, (userId,))
		rows = cursor.fetchall()
		for rs in rows:
			print (rs)
			if userId == rs[1] and userPw == rs[2]:
				session['logFlag'] = True
				session['mNum'] = rs[0]
				session['userId'] = userId
				session["attend"] = rs[0]
				return redirect(url_for('main'))
			else:
				return redirect(url_for('login'))

@app.route('/logout')
def logout():
	session.clear()
	return redirect(url_for('main'))

@app.route('/attend')
def attend():
	if session['attend'] == 0:
		return '이미 출석되었습니다'
	else:
		return render_template('attend.html')

@app.route('/attend_p',methods=('GET','POST'))
def attend_p():
	if request.method == 'POST':
		attend = request.form['date']
		mNum = session['mNum']
		tNum = request.form['tNum']
		
		if len(attend) != 6 or tNum==0:
			return '다시 입력해주세요'
		else:
			db = sqlite3.connect('data.db')
			db.execute(
				'INSERT INTO management (mNum,tNum,attend) VALUES (?,?,?)',
				(mNum,tNum,attend)
			)
			db.commit()
			session["attend"] = 0
			db.close()
			return render_template('main.html')

def select():
	conn = sqlite3.connect('data.db')
	cursor = conn.cursor()
	sql = 'select * from management where mNum = ?'
	cursor.execute(sql,(session['mNum'],))
	rows = cursor.fetchall()
	conn.close()
	return rows

def list_test():
	list = select()
	print(list)

@app.route('/lists')	
def lists():
	lists = select()
	return render_template('lists.html',lists = lists)

app.secret_key = 'sample_secret_key'

if __name__ == '__main__':
	app.debug = True
	app.run(host = '127.0.0.1',port=5000)