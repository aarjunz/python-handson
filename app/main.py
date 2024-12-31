from fastapi import FastAPI

from app.routers import root, predict

app = FastAPI()

# Include routers
app.include_router(root.router)
app.include_router(predict.router)
