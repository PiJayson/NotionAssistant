from abc import ABC, abstractmethod

class IDataHandler(ABC):
    @abstractmethod
    def get_rows(self, database, number_of_rows: int = None, sorted_by: str = None, asc: bool = True):
        pass