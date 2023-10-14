from abc import ABC, abstractmethod
from utils.I_database import IDatabase

class INotionDatabase(IDatabase):
    @abstractmethod
    def get_notion_database_id(self):
        pass
    
    @abstractmethod
    def parse_data(self, data: str):
        pass