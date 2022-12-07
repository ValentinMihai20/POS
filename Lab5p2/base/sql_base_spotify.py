from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
engine = create_engine('mariadb+pymysql://db-admin:db-admin@192.168.56.10:3306/spotify',
                       connect_args={"check_same_thread": False}, echo=True)
sess = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def connect_to_db():
    db = sess()
    try:
        yield db
    finally:
        db.close()
