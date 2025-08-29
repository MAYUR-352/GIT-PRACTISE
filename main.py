from fastapi import FastAPI

app = FastAPI()

todos = []


@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI ToDo App"}


@app.get("/todos")
def get_todos():
    return todos


@app.post("/todos")
def add_todo(item: str):
    todos.append(item)
    return {"message": "Todo added successfully", "todos": todos}
