from utils.tasks_database import TaskDatabase
from rest.I_data_handler import IDataHandler

class DatabaseFactory():
    
    def __init__(self, data_handler: IDataHandler):
        self.data_handler = data_handler
    
    def get_task_database(self):
        return TaskDatabase(self.data_handler)