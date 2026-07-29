from fastapi import FastAPI, HTTPException, Query
from typing import Optional


app = FastAPI(
    title="Greeting API",
    description="A simple API for sending personalized greetings",
)


@app.get("/greet")
def greet_name(name: str = Query(...)):
    """Get a greeting message with the provided name."""
    if not name or len(name.strip()) == 0:
        raise HTTPException(status_code=400, detail="Name cannot be empty.")
    
    return {"message": f"Hello {name}!"}


@app.post("/greet")
def greet_post_name(
    name: str = Query(...),
):
    """Get a greeting message via POST request."""
    if not name or len(name.strip()) == 0:
        raise HTTPException(status_code=400, detail="Name cannot be empty.")
    
    return {"message": f"Hello {name}!"}


@app.get("/")
def read_root():
    """Root endpoint with API documentation."""
    return {"name": "Greeting Service", "status": "running"}
