from rest.I_data_handler import IDataHandler  # Assuming you have your IDataSource interface
from utils.I_notion_database import INotionDatabase
import requests
from decouple import config

# Create a class that communicates with the Notion API
class NotionDataHandler(IDataHandler):
    def __init__(self):
        self.notion_token = config("NOTION_API_TOKEN")
        
        # Initialize the Notion client
        self.headers = {
            "Authorization": "Bearer " + self.notion_token,
            "Content-Type": "application/json",
            "Notion-Version": "2022-06-28",
        }

    def get_rows(self, database: INotionDatabase, number_of_rows: int = None, sorted_by: str = None, asc: bool = True):
        """
        If num_pages is None, get all pages, otherwise just the defined number.
        """
        
        sorting_criteria = [
        {
            "property": sorted_by,  # Replace with the name of the property you want to sort by
            "direction": "ascending" if asc else "descending"    # or "descending" as needed
        }
    ]
        
        get_all = number_of_rows is None
        page_size = 100 if get_all else number_of_rows
        
        database_id = database.get_notion_database_id()
        url = f"https://api.notion.com/v1/databases/{database_id}/query"

        payload = {"page_size": page_size}
        if sorted_by is not None:
            payload["sorts"] = sorting_criteria
        response = requests.post(url, json=payload, headers=self.headers)

        data = response.json()
        if "results" in data:
            results = data["results"]
            while data["has_more"] and get_all:
                payload = {"page_size": page_size, "start_cursor": data["next_cursor"]}
                url = f"https://api.notion.com/v1/databases/{database_id}/query"
                response = requests.post(url, json=payload, headers=self.headers)
                data = response.json()
                results.extend(data["results"])
        
        return results


    def save_data(self):
        pass