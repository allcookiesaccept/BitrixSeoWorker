from services.google_sheets import GoogleSheet
import pandas as pd
from config.logger import logger

class SettingsLoader:
    def __init__(self):
        logger.info("Starting SettingsLoader")
        self.sheet_worker = GoogleSheet()

    def __call__(self, spreadsheet_id: str = spreadsheet_id) -> pd.DataFrame:
        self.sheet_worker(spreadsheet_id)
        self.settings_df = self.sheet_worker.sheet_data
        return self.settings_df


