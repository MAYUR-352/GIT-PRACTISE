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

# this code from hello-world branch
@app.get("/a")
def reada_root():
    return {"message": "Welcome to a FastAPI ToDo App"}

@app.get("/b")
def readb_root():
    return {"message": "Welcome to b FastAPI ToDo App"}

@app.get("/c")
def readc_root():
    return {"message": "Welcome to c FastAPI ToDo App"}