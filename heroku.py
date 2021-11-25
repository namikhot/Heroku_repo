from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from ONLY_WORK_IN_HERE.frontend_main import basic_function

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)


@app.get("/")
def index():
    s = basic_function()
    return {"greeting": s}
