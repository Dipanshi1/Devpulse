import httpx
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {"message": "DevPulse API is running"}
@app.get("/developers/{username}")
def get_developers(username: str):
    url = f"https://api.github.com/users/{username}"
    response = httpx.get(url)
    data = response.json()
    return {
    "username": data["login"],
    "name": data["name"],
    "followers": data["followers"],
    "following": data["following"],
    "public_repos": data["public_repos"],
    "avatar_url": data["avatar_url"],
    "profile_url": data["html_url"],
    "bio": data["bio"],
    "company": data["company"],
    "location": data["location"],
}