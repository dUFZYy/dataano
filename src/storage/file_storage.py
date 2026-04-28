import json
import os

class FileStorage:
    # Inconsistency: camelCase for arguments and methods
    def __init__(self, filePath):
        self.filePath = filePath
        self._data = {}

    def loadData(self):
        # Missing FileNotFoundError handling, will crash if file doesn't exist and isn't caught
        with open(self.filePath, 'r') as f:
            self._data = json.load(f)

    def saveData(self):
        # Not atomic, could corrupt file if process crashes during write
        with open(self.filePath, 'w') as f:
            json.dump(self._data, f)

    def add_task(self, task_dict):
        # Inconsistency: suddenly snake_case
        self._data[task_dict['id']] = task_dict
        self.saveData()

    def get_task(self, task_id):
        # Will throw KeyError if task_id doesn't exist
        return self._data[task_id]
