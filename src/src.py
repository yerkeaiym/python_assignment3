import jwt
from base64 import b64decode
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:12345@localhost/testDb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'thisismyflasksecretkey'

db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key = True)
    login = db.Column(db.String(20))
    password = db.Column(db.String(20))
    token = db.Column(db.String(200))
    
    def __init__(self, login, password):
        self.login = login
        self.password = password
        self.token =  jwt.encode({login : password}, app.secret_key, algorithm = "HS256")
        
@app.route('/', methods = ['GET', 'POST'])
def index():
    names = ['login123', 'loginlogin', 'username']
    passwords = ['password123', 'passpass', 'password']
    for i in range(3):
        if db.session.query(User).filter(User.login == names[i]).count() == 0:
            data = User(names[i],passwords[i])
            db.session.add(data)
    db.session.commit()
    return render_template('login.html')
    
    

@app.route('/submit', methods = ['POST'])
def submit():
    checkLog = request.form['login']
    checkPas = request.form['password']

    if request.method == 'POST':
        res = db.session.query(User)
        for r in res:
            if r.login == checkLog and r.password == checkPas:
                return render_template('successLog.html', data = r.token)
        return render_template('failLog.html', data = checkLog)


@app.route('/protected', methods = ['GET'])
def protected():
    checkTok = request.args.get('token')
    try:
        jwt.get_unverified_header(checkTok)
        return render_template('successProt.html')
    except:
        return render_template('failProt.html')
 
if __name__ == '__main__':
    app.run()