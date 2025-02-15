import subprocess
import json
import os
from app.llm import parse_task

DATA_DIR = "/data"  # Ensure all tasks operate within this directory

def execute_task(task_description: str):
    structured_task = parse_task(task_description)

    if structured_task["task_type"] == "install_uv":
        return install_uv_and_run_script(structured_task["user_email"])
    elif structured_task["task_type"] == "format_markdown":
        return format_markdown_file(structured_task["file_path"])
    elif structured_task["task_type"] == "count_wednesdays":
        return count_wednesdays(structured_task["file_path"], structured_task["output_file"])
    else:
        raise ValueError("Unknown task type")

def install_uv_and_run_script(user_email):
    subprocess.run(["pip", "install", "uv"], check=True)
    subprocess.run(["python", "datagen.py", user_email], check=True)
    return "Data generation complete."

def format_markdown_file(file_path):
    subprocess.run(["npx", "prettier@3.4.2", "--write", file_path], check=True)
    return f"Formatted {file_path}"

def count_wednesdays(file_path, output_file):
    from datetime import datetime

    with open(file_path, "r") as f:
        dates = f.readlines()

    wednesday_count = sum(1 for date in dates if datetime.strptime(date.strip(), "%Y-%m-%d").weekday() == 2)
    
    with open(output_file, "w") as f:
        f.write(str(wednesday_count))
    
    return f"Counted {wednesday_count} Wednesdays in {file_path}"
