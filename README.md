# 🚀 FastAPI Gemini Text Refiner

A high-performance API built with **FastAPI** and **Google Gemini AI** designed to refine, polish, and optimize text input. It features a custom-built **Sliding Window Rate Limiter** to manage API traffic and protect against resource exhaustion.

## ✨ Key Features
* **AI-Powered Refinement:** Leverages `gemini-3.1-flash-lite-preview` for intelligent text enhancement and grammar correction.
* **Custom Rate Limiting:** Implements a sliding window algorithm to differentiate between authenticated and guest users.
* **Robust Error Handling:** Gracefully manages Google API Quota limits (`429 ResourceExhausted`) and validation errors.
* **Pydantic Data Validation:** Ensures strict data integrity for all incoming requests and outgoing responses.
* **Interactive Documentation:** Fully documented API with **Swagger UI** and **ReDoc**.

## 🛠️ Tech Stack
* **Framework:** FastAPI
* **AI Engine:** Google Generative AI (Gemini SDK)
* **Validation:** Pydantic v2
* **Environment:** Python-dotenv
* **Server:** Uvicorn

## ⚙️ Setup & Installation

1\. **Clone the repository:**
   ```bash
   git clone https://github.com/bryanlontoc06/fastapi_gemini_refiner.git
   cd fastapi-gemini-refiner
   ```

2\. **Set up Virtual Environment:**
   ```bash
   python -m venv .venv
   # Windows
   . .venv\Scripts\activate
   # Linux/Mac
   source .venv/bin/activate
   ```

3\. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4\. **Configure Environment Variables:**
   ```bash
   Create a ``.env`` file in the root directory:
   GEMINI_API_KEY={{gemini_api_key}}
   SECRET_KEY={{secret_key}}
   ALGORITHM={{algorithm}}
   AUTH_RATE_LIMIT={{value}}
   AUTH_TIME_WINDOW_SECONDS={{value}}
   GLOBAL_RATE_LIMIT={{value}}
   GLOBAL_TIME_WINDOW_SECONDS={{value}}
   ```

## 🚀 Usage
Start the development server:

```bash
uvicorn src.main:app --reload

Once running, access the interactive documentation at:
- Swagger UI: http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc
```

### LIVE: https://fastapi-gemini-refiner.onrender.com/docs
