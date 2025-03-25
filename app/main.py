from fastapi import FastAPI
from app.core.database import Base, engine
from app.api.routes.user_routes import router

# Create tables in the database
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Register API routes 
app.include_router(router, prefix="/api", tags=["Users"])

@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI with SQLAlchemy!"}
