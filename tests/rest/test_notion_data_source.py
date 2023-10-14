import unittest
from unittest.mock import Mock, patch

import sys
import os

# Add the project root directory to the Python path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.insert(0, project_root)

from src.utils.tasks_database import TaskDatabase
from src.rest.notion_data_source import NotionDataSource  # Import the NotionDataSource class from your module

DATABASE_ID  = 'de6262576a074f5a8d79e1ed6b1e6456'

class TestNotionDataSource(unittest.TestCase):
    @patch('requests.post')
    def test_get_rows(self, mock_post):
        # Mock the requests.post method to return sample data
        mock_post.return_value.json.return_value = {
            "results": [{"id": "123", "properties": {"Name": {"title": [{"plain_text": "Task 1"}]}}}],
            "has_more": False
        }

        # Create an instance of NotionDataSource with a mock token
        notion_data_source = NotionDataSource("mock_token")

        # Create a mock INotionDatabase
        class MockDatabase(TaskDatabase):
            def parse_data(self, row):
                return {"id": row["id"], "name": row["properties"]["Name"]["title"][0]["plain_text"]}

        # Create a mock database and pass it to get_rows
        mock_database = MockDatabase(DATABASE_ID)
        results = notion_data_source.get_rows(mock_database)

        # Assert that the results match the expected data
        expected_results = [{"id": "123", "name": "Task 1"}]
        self.assertEqual(results, expected_results)

if __name__ == "__main__":
    unittest.main()
