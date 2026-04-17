from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# database connection
from backend.database import Base, engine

# import routers correctly
from backend.routes.eco_game_routes import router as eco_game_router
from backend.routes.ai_routes import router as ai_router
from backend.routes.eco_dna_routes import router as eco_dna_router


# create database tables automatically
Base.metadata.create_all(bind=engine)


# create FastAPI app
app = FastAPI(title="EcoLens Backend")


# allow frontend to connect (important for hackathon demo)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # later restrict in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# register route modules
app.include_router(eco_game_router)
app.include_router(ai_router)
app.include_router(eco_dna_router)


# test route
@app.get("/")
def home():
    return {"message": "EcoLens backend running successfully"}