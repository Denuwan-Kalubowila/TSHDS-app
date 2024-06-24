from fastapi import FastAPI
from routers.user_routes import user_router

app=FastAPI()
app.include_router(user_router)