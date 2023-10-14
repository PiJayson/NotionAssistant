from abc import ABC, abstractmethod
from src.utils.I_notion_database import INotionDatabase

class IDataSource(ABC):
    @abstractmethod
    def get_rows(self, database: INotionDatabase, number_of_rows: int):
        pass