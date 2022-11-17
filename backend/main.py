from fastapi import FastAPI, status, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from database import Base, engine, Employee

from sqlalchemy.orm import Session
from schemas import EmployeeSchema, EmployeeUpdateSchema


Base.metadata.create_all(bind=engine)

WHITELIST_CORS_ORIGINS = [
    "http://localhost:8081",
]

app = FastAPI()

app.add_middleware(
    CORSMiddleware, allow_origins=WHITELIST_CORS_ORIGINS, allow_credentials=True,
    allow_methods=["*"], allow_headers=["*"],
)


@app.get("/all_employees", status_code=status.HTTP_200_OK)
def get_all_employees():
    with Session(bind=engine, expire_on_commit=False) as session:
        employees = session.query(Employee).all()

    return employees


@app.post("/employees", status_code=status.HTTP_201_CREATED)
def create_employee(employee_details: EmployeeSchema):
    with Session(bind=engine, expire_on_commit=False) as session:
        employee = Employee(
            employee_first_name=employee_details.employee_first_name,
            employee_last_name=employee_details.employee_last_name
        )
        session.add(employee)
        session.commit()

    return employee_details


@app.get("/employees/{id}", status_code=status.HTTP_200_OK)
def get_employee(id):
    with Session(bind=engine, expire_on_commit=False) as session:
        employee = session.query(Employee).get(id)

    if not employee:
        raise HTTPException(
            detail=f"No Employee found with id: {id}", status_code=status.HTTP_404_NOT_FOUND)

    return employee


@app.patch("/employees/{id}", status_code=status.HTTP_200_OK, response_model=EmployeeSchema)
def update_employee(id, employee_details: EmployeeUpdateSchema):
    with Session(bind=engine, expire_on_commit=False) as session:
        employee = session.query(Employee).get(id)

        if not employee:
            raise HTTPException(
                detail=f"No Employee found with id: {id}", status_code=status.HTTP_404_NOT_FOUND)

        # keys = employee_details.__dict__.keys()
        # print(employee_details.__dict__)
        # for key in keys:
        #     if hasattr(employee, key):
        #         employee.key = employee_details.__dict__.get(key)

        employee.employee_first_name = employee_details.employee_first_name
        employee.employee_last_name = employee_details.employee_last_name
        session.commit()

        return employee_details


@app.delete("/employees/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_employee(id):
    with Session(bind=engine, expire_on_commit=False) as session:
        employee = session.query(Employee).get(id)

        if not employee:
            raise HTTPException(
                detail=f"No Employee found with id: {id}", status_code=status.HTTP_404_NOT_FOUND)

        session.delete(employee)
        session.commit()

    