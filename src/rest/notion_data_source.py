from src.rest.I_data_source import IDataSource  # Assuming you have your IDataSource interface
from src.utils.I_notion_database import INotionDatabase
import requests

# Create a class that communicates with the Notion API
class NotionDataSource(IDataSource):
    def __init__(self, notion_token):
        # Initialize the Notion client
        self.headers = {
            "Authorization": "Bearer " + notion_token,
            "Content-Type": "application/json",
            "Notion-Version": "2022-06-28",
        }

    def get_rows(self, database: INotionDatabase, number_of_rows: int = None):
        """
        If num_pages is None, get all pages, otherwise just the defined number.
        """
        
        get_all = number_of_rows is None
        page_size = 100 if get_all else number_of_rows
        database_id = database.get_notion_database_id()
        url = f"https://api.notion.com/v1/databases/{database_id}/query"

        payload = {"page_size": page_size}
        response = requests.post(url, json=payload, headers=self.headers)

        data = response.json()

        results = data["results"]
        while data["has_more"] and get_all:
            payload = {"page_size": page_size, "start_cursor": data["next_cursor"]}
            url = f"https://api.notion.com/v1/databases/{database_id}/query"
            response = requests.post(url, json=payload, headers=self.headers)
            data = response.json()
            results.extend(data["results"])
        
        # Parse data
        final_result = []
        for row in results:
            parsed_data = database.parse_data(row)
            final_result.append(parsed_data)
        
        return final_result


    def save_data(self):
        pass