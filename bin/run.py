import uvicorn

if __name__ == "__main__":
    uvicorn.run("fastapi_best_practice.main:app", host="0.0.0.0")
