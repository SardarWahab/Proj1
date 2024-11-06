# save this as app.py
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
app = Flask(__name__)
# adding configuration for using a sqlite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False  

# Creating an SQLAlchemy instance
db = SQLAlchemy(app)
migrate = Migrate(app,db)


#database classes

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(20), nullable=False)



class Subject(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        subject_name = db.Column(db.String(20), nullable=False)
        subject_code = db.Column(db.String(20), nullable=False)
@app.route("/")
def hello():
    return render_template('index.html')


@app.route("/about")
def about():
    return render_template('about.html')


@app.route("/contact")
def contact():
    return render_template('contact.html')



if __name__ == '__main__':
    app.run(debug=True)