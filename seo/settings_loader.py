from services.google_sheets import GoogleSheet
from seo.settings_counter import SettingsCounter
import pandas as pd
from config.logger import logger

class SettingsLoader:
    def __init__(self, service_file_path: str, google_sheet: str):
        logger.info("Starting SettingsLoader")
        self.sheet_worker = GoogleSheet(service_file_path)
        self.counter = SettingsCounter()

    def __call__(self, spreadsheet_id: str) -> pd.DataFrame:
        self.sheet_worker(spreadsheet_id)
        self.settings_df = self.sheet_worker.sheet_data
        return self.settings_df
