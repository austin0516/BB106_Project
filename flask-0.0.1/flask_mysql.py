from flask import Flask  
# from flask.ext.sqlalchemy import SQLAlchemy
from flask_sqlalchemy import SQLAlchemy  
from sqlalchemy import Table, Column, Integer, String, Date, Float  
# import config    
  
# DB class  
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
    #playerid = db.Column('playerid', Integer, primary_key=True)  
    #username = db.Column('username', String(30), unique=True)  
    #email = db.Column('email', String(50), unique=True)  
    #password = db.Column('password', String(100), unique=False)  
    #avatarid = db.Column('avatarid', Integer,default=1)  
    #language = db.Column('language', Integer,default=1)  
    #regdate = db.Column('regdate', Date)  
    #activation_key = db.Column('activation_key', String(60))  
    #active = db.Column('active', Integer, default=0)  
   
    def __init__():  
        return
        #self.username = username  
        #self.email = email  
        #self.password = password  
   
    def __repr__(self):  
        return '<Person %s %s>' % (str(self.id), self.name)  

# route
@app.route('/persons/')
def list_persons():  
    persons = Person.query.all()  
    #app.logger.debug(&quot;Player length %s &quot;, len(players))  
    #a = &quot;&quot;  
    d = {} 
    a = "" 
    for p in persons:  
       app.logger.debug(p.name)  
       a = a + " " + p.name  
       #a = p.name  
    return "Hello Persons: %s "  % (a)  


@app.route('/')
def index():
    return "Hello, World!"





if __name__ == '__main__':  
    #create table from up model  
    #db.create_all()
    app.run(host='127.0.0.1', debug=True)  
