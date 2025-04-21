from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routes.agentic_routes import router as agentic_router

app = FastAPI()

origins = ["http://localhost:3000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(agentic_router)


# FastAPI: This is the main FastAPI app class used to create your API.

# CORSMiddleware: Middleware to handle CORS (Cross-Origin Resource Sharing). 
# It's needed when your frontend (e.g., React running on localhost:3000) tries to make requests 
# to your backend (localhost:8000).

# router as agentic_router: You’re importing a router (likely where your API routes/endpoints are defined) 
# from a file called agentic_routes.py in the routes folder, and giving it the alias agentic_router.