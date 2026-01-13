from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

database_url = "mysql+pymysql://root:Mysqlroot%4025@localhost/book_management_db"

engine = create_engine(database_url)
sessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

base = declarative_base()