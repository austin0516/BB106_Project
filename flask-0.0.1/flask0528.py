from flask import Flask  
# from flask.ext.sqlalchemy import SQLAlchemy
from flask_sqlalchemy import SQLAlchemy
import os  
from sqlalchemy import Table, Column, Integer ,String, Date, Float
from flask import render_template, request
# import config 

app = Flask(__name__)
db_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "test.db")
# mysql://user:password@host:port/dbname
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://test:test@127.0.0.1:3306/test"
db = SQLAlchemy(app) 

# DB classess  

class liu_table(db.Model):
    tablename = 'liu_table'

    Stockcode = db.Column(db.String(255), primary_key=True)
    Method = db.Column(db.String(255), primary_key=True)
    Fitnessvalue_withoutGA = db.Column(db.Float)
    Fitnessvalue_withGA = db.Column(db.Float)
    Picture_withGA = db.Column(db.String(255))
    GA_picture = db.Column(db.String(255))


class text_mining_table(db.Model):
    tablename = 'text_mining_table'

    title = db.Column(db.String(255), primary_key=True)
    url = db.Column(db.String(255))
    picture = db.Column(db.String(255))


@app.route('/', methods=['GET', 'POST'])
def hello_world():
    EID = db.session.query(liu_table.Stockcode).distinct()
    METHOD_NAME = db.session.query(liu_table.Method).distinct()
    TID = text_mining_table.query.all()
    
#    if 'pid' in request.form and 'pname' in request.form:       
#        the_two = Person.query.filter_by(id=int(request.form.get('pid')), name=(request.form.get('pname')))
#        pid = request.form.get('pid', 0, type=int)
#        the_one = Person.query.get(pid)      
#        return render_template("index.html", ID=ID, NAME=NAME, the_two=the_two)
    
    if 'eid' in request.form and 'method' in request.form:
        result = liu_table.query.filter_by(Stockcode=(request.form.get("eid")), Method=request.form.get("method"))
        return render_template("index.html", EID=EID, METHOD_NAME=METHOD_NAME, result=result)

    
    if 'tid' in request.form:
        tid = request.form.get('tid')
        the_one = text_mining_table.query.get(tid)
        return render_template("index.html", TID=TID, the_one=the_one)

   

    
    return render_template("index.html", EID=EID, METHOD_NAME=METHOD_NAME, TID=TID)

if __name__ == '__main__':
    app.run()


