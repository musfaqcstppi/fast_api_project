from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:your_password@localhost:3306/test_db"
SQLALCHEMY_DATABASE_URL = "postgresql+psycopg2://training_jls0_user:h3daqQFGBaycKf2aK9n9iL5SaFIPJiA6@dpg-dbbfgmeq1p3s73cefugg-a.oregon-postgres.render.com/training_jls0"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()