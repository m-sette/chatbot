from fastapi import FastAPI
from app.routes import question
from multiprocessing import Process
from app.services.app import run_slack_app

app = FastAPI()

# handle all routes defined in the '/question' router
app.include_router(question.router)

def run_uvicorn_app():
    import uvicorn
    uvicorn.run("main:app", reload=True)

if __name__ == "__main__":
    api_thread = Process(target=run_uvicorn_app)
    api_thread.start()

    run_slack_app()