import os
from http import HTTPStatus

from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.responses import JSONResponse

from src.models import RefineRequest, RefineResponse

from .ai.gemini import Gemini

# --- App Initialization ---
load_dotenv()
app = FastAPI()


# --- AI Configuration ---
def load_system_prompt():
    try:
        with open("src/prompts/system_prompt.md", "r") as f:
            return f.read()
    except FileNotFoundError:
        return None

system_prompt = load_system_prompt()
gemini_api_key = os.getenv("GEMINI_API_KEY")

if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY is not set in the environment variables.")

ai_platform = Gemini(api_key=gemini_api_key, system_prompt=system_prompt)

# --- Endpoints ---
@app.get("/")
def root():
    return {"message": "Welcome to the AI Refiner!"}

@app.post("/refine", response_model=RefineResponse, tags=["Refine"], operation_id="refine")
def refine(refine_request: RefineRequest):
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
    refined_message = ai_platform.refine(refine_request.message)
    return RefineResponse(response=refined_message)
