from fastapi import FastAPI, Query, HTTPException
import os
from app.task_handler import execute_task
from app.utils import read_file

app = FastAPI(title="Automation Agent", version="1.0")

# Run task endpoint
@app.post("/run")
async def run_task(task: str = Query(..., description="Describe the task in plain English")):
    try:
        result = execute_task(task)
        return {"status": "success", "message": result}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Read file endpoint
@app.get("/read")
async def read_file_api(path: str = Query(..., description="Path of the file to read")):
    try:
        content = read_file(path)
        return {"status": "success", "content": content}
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="File not found")
