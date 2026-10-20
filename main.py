from fastapi import FastAPI
import models
from database import engine
from routers import user_controller

# Create tables in MySQL automatically if they don't exist
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="FastAPI MySQL Clean Architecture CRUD")

# Register the controller routes
app.include_router(user_controller.router)