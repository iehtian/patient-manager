from backend.pgsql_server import select_all_patients,select_patients_by_name,add_patient
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from datetime import date

class PatientCreate(BaseModel):
    name: str
    birthDate: date
    gender: str


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173","http://localhost:5174"],  # Vue 开发服务器地址
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/patients")
async def get_patients(search: str = ""):
    patients = select_patients_by_name(search)
    return {"patients": patients}

@app.post("/add_patients")
async def create_patient(patient: PatientCreate):
    print( patient.name, patient.birthDate, patient.gender)
    add_patient(patient.name, patient.birthDate, patient.gender)
    return {"message": "Patient added successfully"}

def main():
    patients = select_all_patients()
    for patient in patients:
        print(patient)
		
if __name__ == "__main__":
	main()
