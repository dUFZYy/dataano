import pytest
from src.storage.file_storage import FileStorage

def test_file_storage_add():
    # Flaw: Uses a hardcoded test file in the current directory and doesn't clean it up
    fs = FileStorage("test_data.json")
    
    task_data = {"id": "123", "title": "Test", "status": "pending"}
    fs.add_task(task_data)

    # Flaw: Missing actual assertions! Just checks if it runs without crashing.
