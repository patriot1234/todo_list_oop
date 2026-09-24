from datetime import datetime

class Task:
    def __init__(self, id:int, title: str, created_at: str=None, status= False):
        self.id=id
        self.title=title
        self.created_at=created_at or datetime.now().strftime("%Y-%m-%d  %H:%M")
        self.status=status

    def __str__(self):
        return f"{self.id}\t{self.title}\t{self.created_at}\t{self.status}\n"

    def task_dict(self):
        return {"id" : self.id , "title" :self.title , "created_at":self.created_at , "status" : self.status}
    

