from mysql_server import select_all_painters
from fastapi import FastAPI

def main():
	painters = select_all_painters()
	for painter in painters:
		print(painter)
		
app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/painters")
async def get_painters():
    painters = select_all_painters()
    return {"painters": painters}

if __name__ == "__main__":
	main()
