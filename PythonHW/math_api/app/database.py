# Logging on the database
import os
from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime
from sqlalchemy.orm import declarative_base, sessionmaker
from datetime import datetime

# Read the connection parameters from environment variables
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "1433")
DB_NAME = os.getenv("DB_NAME", "mathdb")
DB_USER = os.getenv("DB_USER", "sa")
DB_PASSWORD = os.getenv("DB_PASSWORD", "Str0ng_Pa55!")

# SQL Server connection string (ODBC driver neve fix lehet Linuxon)
DATABASE_URL = (
    f"mssql+pyodbc://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    "?driver=ODBC+Driver+17+for+SQL+Server"
)

# Initialization of SQLite database (SQLAlchemy engine and session)
#engine = create_engine("sqlite:///./operations.db", connect_args={"check_same_thread": False})
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()


# Table structure - Model
class OperationLog(Base):
    __tablename__ = "operations"

    id = Column(Integer, primary_key=True, index=True)
    operation = Column(String)
    input1 = Column(Float)
    input2 = Column(Float, nullable=True)
    result = Column(Float)
    timestamp = Column(DateTime, default=datetime.utcnow)


# Database
def init_db():
    Base.metadata.create_all(bind=engine)
