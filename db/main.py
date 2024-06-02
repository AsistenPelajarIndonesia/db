from fastapi import FastAPI
from db.routes import user_route
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*']
)


# Basics AI Providers
app.include_router(user_route.api_router)

@app.get("/")
async def root():
    return {"status": "UP"}
