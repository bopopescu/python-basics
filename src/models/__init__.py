from sqlalchemy import create_engine
# from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Integer, String, Text, Binary, Column
from sqlalchemy.orm import sessionmaker
import uuid



engine = create_engine('mysql+pymysql://root:root@localhost:3306/import_example', convert_unicode=True)
# db_session = scoped_session(sessionmaker(autocommit=False,
#                                          autoflush=False,
#                                          bind=engine))

Session = sessionmaker(bind=engine)

session = Session()



from sqlalchemy.ext.declarative import as_declarative

@as_declarative()
class Base(object):
    id = Column(String(36), primary_key=True, default=str(uuid.uuid4()))