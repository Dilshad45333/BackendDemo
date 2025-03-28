from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.database import Base, engine
from app.routes.user_routes import router

# Create tables in the database
Base.metadata.create_all(bind=engine)

app = FastAPI()
allowed_origins = ["http://192.168.1.7:8081"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,  # Allow all origins (change in production)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# Register API routes 
app.include_router(router, prefix="/api", tags=["Users"])


