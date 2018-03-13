from flask import Flask,render_template,request,redirect,url_for,g,jsonify,session
import os
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////%s/mani.db' % (os.getcwd())
app.config['SECRET_KEY'] = 'super-secret'
db = SQLAlchemy(app)





class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username =  db.Column(db.Boolean, unique=False, default=True)
    passd =  db.Column(db.Text, nullable=False)




@app.route('/')
def index():
    return render_template('index.html',**locals())



@app.route('/user/<username>')
def logout(username):
    
    # import ipdb; ipdb.set_trace()
    if int(username) <= 3:
        return jsonify({'status':True})
    else:
        return jsonify({'status': False})






if __name__=='__main__':
    app.run(debug=True)