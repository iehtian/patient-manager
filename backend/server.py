from backend.pgsql_server import select_all_patients
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


def main():
	patients = select_all_patients()
	for painter in patients:
		print(painter)
		
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
async def get_patients():
    patients = select_all_patients()
    return {"patients": patients}

if __name__ == "__main__":
	main()
