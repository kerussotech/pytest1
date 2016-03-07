from flask import Flask
app = Flask(__name__)

from sqlalchemy import create_engine
engine = create_engine('postgresql+psycopg2://pytest1:pytest1@localhost:5432/pytest1')

from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

from sqlalchemy import Column, Integer, String
class pytest1(Base):
  __tablename__ = 'pytest1'

  id = Column(Integer, primary_key = True)
  first = Column(String)
  last = Column(String)
  type = Column(String)
  description = Column(String)

  def __repr__(self):
    return "%s %s, %s (%s)" % (self.first, self.last, self.description, self.type)

from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)

session = Session()

users = session.query(pytest1).order_by(pytest1.id)

@app.route('/pytest1')

def hello_world():
  for user in users:
    print user
  return 'Hello World!'

if __name__ == '__main__':
    app.run(host='0.0.0.0')

