import sys

# Intentional potential issue: running `python src/main.py` might fail with ModuleNotFoundError
from src.models import Task
from src.storage.file_storage import FileStorage
from src.utils import validateTask
from src.auth import authenticate

def main():
    # Authenticate the user first
    authenticate()

    # Hardcoded path, not configurable via env vars or args
    storage = FileStorage("tasks.json")

    try:
        storage.loadData()
    except Exception as e:
        # Bad practice: broad except clause, hides real errors like permission denied
        print("Failed to load existing tasks. Starting fresh.")

    if len(sys.argv) > 1:
        action = sys.argv[1]
        
        if action == "add":
            # Missing index out of bounds handling if sys.argv[2] doesn't exist
            title = sys.argv[2]
            t = Task(title)
            
            if validateTask(t):
                storage.add_task(t.to_dict())
                print(f"Added task: {t.title}")
            else:
                print("Invalid task parameters.")
                
        elif action == "list":
            # Accessing pseudo-private member directly
            for tid, tdata in storage._data.items():
                print(f"[{tdata['status']}] {tdata['title']}")
                
        else:
            print("Unknown action")
    else:
        print("Usage: python main.py [add|list]")

if __name__ == "__main__":
    main()
