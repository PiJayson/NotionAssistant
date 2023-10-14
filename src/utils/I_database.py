from abc import ABC, abstractmethod

from rest.I_data_handler import IDataHandler

class IDatabase(ABC):
    @abstractmethod
    def __init__(self, data_handler: IDataHandler):
        pass
    
    @abstractmethod
    def get_properties(self):
        pass