from fastapi import FastAPI
from db.routes import users
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*']
)


# Basics AI Providers
app.include_router(users.api_router)

@app.get("/")
async def root():
    return {"status": "UP"}
