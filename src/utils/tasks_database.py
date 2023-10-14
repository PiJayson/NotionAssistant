from src.utils.I_notion_database import INotionDatabase
from src.utils.task_row import TaskRow

class TaskDatabase(INotionDatabase):
    
    def __init__(self, notion_page_url):
        self.notion_page_url = notion_page_url
        
    def get_attributes(self):
        return type(TaskDatabase)
    
    def get_notion_database_id(self):
        return self.notion_page_url
    
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