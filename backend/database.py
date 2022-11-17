from sqlalchemy import Column, String, Integer, create_engine
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("sqlite:///employee_management.db")
Base = declarative_base()


class Employee(Base):
    __tablename__ = "Employee"

    id = Column(Integer, primary_key=True, index=True)
    employee_first_name = Column(String(32))
    employee_last_name = Column(String(32))

Base.metadata.create_all(bind=engine)
