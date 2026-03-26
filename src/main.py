from fastapi import FastAPI

# --- App Initialization ---
app = FastAPI()

# --- Endpoints ---
@app.get("/")
def root():
    return {"message": "Welcome to the AI Refiner!"}