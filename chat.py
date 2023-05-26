from flask import Flask, render_template, request, session, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///chat.db'
db = SQLAlchemy(app)

class User:
    def __init__(self, name, email, gender, age, profession):
        self.name = name 
        self.email = email
        self.gender = gender
        self.age = age 
        self.profession = profession 
obj = User("John","john.doe@unien.ch", None, 0 , None) 

@app.route('/')
def logIn():
    return  render_template('logIn.html', name=obj.name)

@app.route('/create_user', methods=['POST'])
def create_user():
    name = request.form['name']
    email = request.form['email']
    gender = request.form['gender']
    #if gender != "male" or gender != "femmale" or gender != "other":
    #    return render_template
    #faire un message d'erreur maybe 
    # -> trouver comme faire des messages d'erreur comme ceux qui existent déjà ex: impossible de mettre un email sans "@"
    age = request.form['age']
    profession = request.form['profession']
    user = User(name,email,gender,age,profession)
    session['name'] = request.form['name']
    session['email'] = request.form['email']
    session['gender'] = request.form['gender']
    session['age'] = request.form['age']
    session['profession'] = request.form['profession']
    return render_template(
        'home.html', 
        name = name, 
        email=email,
        gender=gender,
        age=age,
        profession=profession)

@app.route('/goToHome', methods=["POST"])
def goToHome():
    name = session.get('name')
    email = session.get('email')
    gender = session.get('gender')
    age = session.get('age')
    profession = session.get('profession')
    return render_template(
        'home.html',
        name = name ,
        email = email,  
        gender = gender,
        age = age,
        profession = profession)

@app.route('/goToAccount')
def goToAccount():
    name = session.get('name')
    email = session.get('email')
    gender = session.get('gender')
    age = session.get('age')
    profession = session.get('profession')
    return render_template(
        'account.html', 
        name = name ,
        email = email,  
        gender = gender,
        age = age,
        profession = profession)

@app.route('/logout')
def logout():
    session.pop('name', None)
    session.pop('email', None)
    session.pop('gender',None)
    session.pop('age',None)
    session.pop('profession',None)
    return redirect(url_for('logIn'))

# A PARTIR DE LA C'EST BAGDAD

@app.route('/goToModifyAccount')
def goToModifyAccount():
    return redirect(url_for('modifyAccount'))

@app.route('/modifyAccount')
def modifyAccount():
    pass
