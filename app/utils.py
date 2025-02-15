import os

def read_file(file_path):
    if not file_path.startswith("/data/"):
        raise PermissionError("Access outside /data/ is not allowed.")

    with open(file_path, "r") as f:
        return f.read()
