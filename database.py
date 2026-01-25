from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

load_dotenv()

DB_URL=os.getenv("DATABASE_URL")

SQLALCHMY_DATABASE_URL = DB_URL

engine = create_engine(SQLALCHMY_DATABASE_URL) # type: ignore
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
