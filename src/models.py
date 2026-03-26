from pydantic import BaseModel


# --- Pydantic Models ---
class RefineRequest(BaseModel):
    message: str

class RefineResponse(BaseModel):
    response: str