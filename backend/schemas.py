from pydantic import BaseModel, main
from typing import Optional


class EmployeeSchema(BaseModel):
    employee_first_name: str
    employee_last_name: str


class EmployeeUpdateSchema(BaseModel):
    employee_last_name: str
    employee_first_name: str
