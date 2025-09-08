import requests
import json
import csv
import logging
import time
import os
from config import HEADERS_TEMPLATE, DATA_DIR, LOG_FILE

class JobScraper:
    def __init__(self, endpoint_config):
        self.url = endpoint_config['url']
        self.headers = HEADERS_TEMPLATE.copy()
        self.headers['x-rapidapi-host'] = endpoint_config['host']
        self.data_dir = DATA_DIR
        os.makedirs(self.data_dir, exist_ok=True)
        self.setup_logging()

    def setup_logging(self):
        logging.basicConfig(
            filename=LOG_FILE,
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s'
        )

    def fetch_data(self, params=None):
        try:
            logging.info(f"Fetching data from {self.url}")
            response = requests.get(self.url, headers=self.headers, params=params)
            response.raise_for_status()
            data = response.json()
            logging.info(f"Successfully fetched {len(data)} items")
            return data
        except requests.exceptions.RequestException as e:
            logging.error(f"Request error: {e}")
            return None
        except json.JSONDecodeError as e:
            logging.error(f"JSON decode error: {e}")
            return None

    def save_to_json(self, data, filename):
        filepath = os.path.join(self.data_dir, filename)
        try:
            with open(filepath, 'w') as f:
                json.dump(data, f, indent=4)
            logging.info(f"Data saved to {filepath}")
        except Exception as e:
            logging.error(f"Error saving to JSON: {e}")

    def save_to_csv(self, data, filename, fields):
        filepath = os.path.join(self.data_dir, filename)
        try:
            with open(filepath, 'w', newline='', encoding='utf-8') as f:
                writer = csv.DictWriter(f, fieldnames=fields)
                writer.writeheader()
                for item in data:
                    writer.writerow({field: item.get(field, '') for field in fields})
            logging.info(f"Data saved to {filepath}")
        except Exception as e:
            logging.error(f"Error saving to CSV: {e}")

    def parse_job_data(self, data):
        # Override in subclasses for specific parsing
        return data

    def run(self, params=None, save_json=True, save_csv=False, csv_fields=None):
        data = self.fetch_data(params)
        if data:
            parsed_data = self.parse_job_data(data)
            if save_json:
                self.save_to_json(parsed_data, f"{self.__class__.__name__.lower()}_data.json")
            if save_csv and csv_fields:
                self.save_to_csv(parsed_data, f"{self.__class__.__name__.lower()}_data.csv", csv_fields)
            return parsed_data
        return None
