from backend.mysql_server import select_all_painters
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


def main():
	painters = select_all_painters()
	for painter in painters:
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

@app.get("/painters")
async def get_painters():
    painters = select_all_painters()
    return {"painters": painters}

if __name__ == "__main__":
	main()
