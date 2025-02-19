import fastapi as FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message":"This Is Just a Landing Page"}