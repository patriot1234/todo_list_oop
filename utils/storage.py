from utils.tasks import Task
from dotenv import load_dotenv
from pathlib import Path
import os
import json

class Storage:
    def __init__(self):
        load_dotenv()
        filename = os.getenv("TASKS_FILE", "tasks.json")

        root = Path(__file__).resolve().parent.parent
        self.file_path = root / filename
        


    def load(self):
        print(self.file_path)

        with self.file_path.open("r", encoding="utf-8") as file:
            obj_list = json.load(file)
    
        return obj_list

    
    def save(self,object):
        with self.file_path.open("w", encoding="utf-8") as file:
            json.dump(object, file, indent=4)

        

