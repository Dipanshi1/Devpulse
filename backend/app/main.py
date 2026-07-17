from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {"message": "DevPulse API is running"}
@app.get("/developers/{username}")
def get_developers(username: str):
    return {"message": f"Developer: {username}"}