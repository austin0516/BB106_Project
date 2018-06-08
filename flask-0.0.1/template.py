from flask import Flask  
# from flask.ext.sqlalchemy import SQLAlchemy
from flask_sqlalchemy import SQLAlchemy  
from sqlalchemy import Table, Column, Integer, String, Date, Float
from flask import render_template, request  
# import config 

app = Flask(__name__)
# mysql://user:password@host:port/dbname
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://test:test@127.0.0.1:3306/test"
db = SQLAlchemy(app) 

# DB classess  
class Person(db.Model):  
    __tablename__ = 'person'  
   
    id = db.Column('id', Integer, primary_key=True)
    name = db.Column('name', String(255))
    age = db.Column('age', Integer)
   
    def __init__():  
        return

    def __repr__(self):  
        return '<Person %s %s>' % (str(self.id), self.name)  







@app.route('/', methods=['GET', 'POST'])
def index():
    persons = Person.query.all()
    if 'pid' in request.form:
        pid = request.form.get('pid', 0, type=int)
        the_one = Person.query.get(pid)
        return render_template('index.html', persons=persons, the_one=the_one)
    return render_template('index.html', persons=persons)

@app.route('/show_wc')
def show_wc():
    return render_template('index.html')



if __name__ == '__main__':
    app.run(host='127.0.0.1', debug=True)
