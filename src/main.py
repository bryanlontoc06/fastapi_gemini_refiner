from http import HTTPStatus

from fastapi import FastAPI
from fastapi.responses import JSONResponse

from src.models import RefineRequest, RefineResponse

# --- App Initialization ---
app = FastAPI()

# --- Endpoints ---
@app.get("/")
def root():
    return {"message": "Welcome to the AI Refiner!"}

@app.post("/refine", response_model=RefineResponse, tags=["Refine"], operation_id="refine")
def refine(refine_request: RefineRequest):
    refined_message = f"{refine_request.message}"
    if len(refine_request.message) > 150:
        return JSONResponse(
            status_code=HTTPStatus.BAD_REQUEST,
            content={
                "error": {
                    "code": HTTPStatus.BAD_REQUEST,
                    "message": f"Message exceeds 150 characters limit. Total characters: {len(refine_request.message)}"
                }
            }
        )
    return RefineResponse(refined_message=refined_message)
