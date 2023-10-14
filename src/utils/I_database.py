from abc import ABC, abstractmethod

class IDatabase(ABC):
    @abstractmethod
    def get_attributes(self):
        pass