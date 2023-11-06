from fastapi import FastAPI
from app.routes import question

app = FastAPI()

# handle all routes defined in the '/question' router
app.include_router(question.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", reload=True)