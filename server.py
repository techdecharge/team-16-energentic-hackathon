from app import app
from app.config import APPLICATION_HOST, APPLICATION_PORT


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host=APPLICATION_HOST, port=APPLICATION_PORT)
