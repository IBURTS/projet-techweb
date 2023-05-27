from flask import Flask, render_template, request, session, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///chat.db'
db = SQLAlchemy(app)

"""
class ExampleUser(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    gender = db.Column(db.String(80), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    profession = db.Column(db.String(80), nullable=False)

    def __init__(self, name, email, gender, age, profession):
        self.name = name
        self.email = email
        self.gender = gender
        self.age = age
        self.profession = profession


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String(80), nullable=False)
    content = db.Column(db.Text)

    def __init__(self, author, content):
        self.author = author
        self.content = content


with app.app_context():
    db.drop_all()
    db.create_all()
"""


class User:
    def __init__(self, name, email, gender, age, profession):
        self.name = name
        self.email = email
        self.gender = gender
        self.age = age
        self.profession = profession


obj = User("John", "john.doe@unien.ch", None, 0, None)


@app.route('/')
def logIn():
    return render_template('logIn.html', name=obj.name)


@app.route('/create_user', methods=['POST'])
def create_user():
    name = request.form['name']
    email = request.form['email']
    gender = request.form['gender']
    # if gender != "male" or gender != "female" or gender != "other":
    #    return render_template
    # faire un message d'erreur maybe
    # -> trouver comme faire des messages d'erreur comme ceux qui existent déjà ex: impossible de mettre un email sans "@"
    age = request.form['age']
    profession = request.form['profession']
    user = User(name, email, gender, age, profession)
    session['name'] = request.form['name']
    session['email'] = request.form['email']
    session['gender'] = request.form['gender']
    session['age'] = request.form['age']
    session['profession'] = request.form['profession']
    return render_template(
        'home.html',
        name=name,
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
        name=name,
        email=email,
        gender=gender,
        age=age,
        profession=profession)


@app.route('/goToAccount')
def goToAccount():
    name = session.get('name')
    email = session.get('email')
    gender = session.get('gender')
    age = session.get('age')
    profession = session.get('profession')
    return render_template(
        'account.html',
        name=name,
        email=email,
        gender=gender,
        age=age,
        profession=profession)


@app.route('/logout')
def logout():
    session.pop('name', None)
    session.pop('email', None)
    session.pop('gender', None)
    session.pop('age', None)
    session.pop('profession', None)
    return redirect(url_for('logIn'))


# A PARTIR DE LA C'EST BAGHDAD


@app.route('/goToModifyAccount')
def goToModifyAccount():
    return redirect(url_for('modifyAccount'))


@app.route('/modifyAccount')
def modifyAccount():
    pass
