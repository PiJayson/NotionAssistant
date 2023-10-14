from decouple import config

# REST
from utils.I_notion_database import INotionDatabase
from utils.task_row import TaskRow
from utils.task_properties import TaskProperties
from rest.I_data_handler import IDataHandler

class TaskDatabase(INotionDatabase):
    
    def __init__(self, data_handler: IDataHandler):
        self.data_handler = data_handler
        self.database_id = config('TASK_DATABASE_ID')
        
    def get_properties(self) -> TaskProperties:
        return TaskProperties
    
    def get_notion_database_id(self):
        return self.database_id
    
    def get_rows(self, number_of_rows: int = None, sorted_by: str = None, asc: bool = True):
        rows = self.data_handler.get_rows(self, number_of_rows, sorted_by, asc)
        
        result = []
        for row in rows:
            result.append(self.parse_data(row))
        
        return result
    
    def parse_data(self, data: str):
        props = data["properties"]
        task_name = props["Task name"]["title"][0]["text"]["content"]
        status = props["Status"]["status"]["name"]
        assignee = props["Assignee"]["people"]
        due_start = props["Due"]["date"]["start"]
        due_end = props["Due"]["date"]["end"]
        priority = props["Priority"]["select"]
        tags = props["Tags"]["multi_select"]
        projects = props["Project"]["relation"]
        
        return TaskRow(task_name, status, assignee, (due_start, due_end), priority, tags, projects)