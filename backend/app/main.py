

import httpx
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {"message": "DevPulse API is running"}
@app.get("/developers/{username}")
def get_developers(username: str):
    url = f"https://api.github.com/users/{username}"
    user_response = httpx.get(url)
    user_data = user_response.json()
    repos_url = f"https://api.github.com/users/{username}/repos"
    total_stars = 0
    total_forks = 0
    repos_response = httpx.get(repos_url)
    repos_data = repos_response.json()
    for repo in repos_data:
        total_stars += repo["stargazers_count"]
        total_forks += repo["forks_count"]

    return {
        "username": user_data["login"],
        "name": user_data["name"],
        "followers": user_data["followers"],
        "following": user_data["following"],
        "public_repos": user_data["public_repos"],
        "avatar_url": user_data["avatar_url"],
        "profile_url": user_data["html_url"],
        "bio": user_data["bio"],
        "company": user_data["company"],
        "location": user_data["location"],
        "total_stars": total_stars,
        "total_forks": total_forks
    }
