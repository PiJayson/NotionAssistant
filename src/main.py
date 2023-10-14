# UI
from ui.menu import Menu

from decouple import config

# REST
from rest.notion_data_handler import NotionDataHandler
from utils.database_factory import DatabaseFactory


if __name__ == "__main__":
    notion_data_handler = NotionDataHandler()
    database_factory = DatabaseFactory(notion_data_handler)

    Menu(database_factory).run()