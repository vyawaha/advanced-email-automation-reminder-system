from fastapi import FastAPI

app = FastAPI(
    title="Email Automation API",
    version="1.0"
)


@app.get("/")
def home():
    return {
        "message": "Email Automation System Running"
    }