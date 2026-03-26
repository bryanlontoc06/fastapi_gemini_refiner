from pydantic import BaseModel

# --- Pydantic Models ---
class RefineRequest(BaseModel):
    input_text: str

class RefineResponse(BaseModel):
    refined_text: str