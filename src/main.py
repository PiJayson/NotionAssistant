# Example usage
from decouple import config
from rest.notion_data_source import NotionDataSource
from utils.tasks_database import TaskDatabase
from datetime import datetime

NOTION_TOKEN = config('NOTION_API_TOKEN')
DATABASE_ID  = 'de6262576a074f5a8d79e1ed6b1e6456'

notion_database = NotionDataSource(NOTION_TOKEN)
task_database = TaskDatabase(DATABASE_ID)

for row in notion_database.get_rows(task_database, 10):
    row.print()