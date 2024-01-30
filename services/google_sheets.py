import pygsheets
from pathlib import Path
from config.logger import logger
from config.config import DataManager

class GoogleSheet:
    def __init__(self, service_file_path: str, spreadsheet_id: str):
        self.service_file_path = service_file_path
        self.spreadsheet_id = spreadsheet_id
        logger.info("Starting GoogleSheet")

    def __call__(self):
        self.__oauth()
        self.open_spreadsheet(self.spreadsheet_id)
        self.get_spreadsheet()

    def __spreadsheet_connection_check(self):
        if self.sheet is None:
            raise ValueError(
                "Spreadsheet is not opened. Call `open_spreadsheet()` first."
            )

    def __oauth(self):
        self.__oauth = pygsheets.authorize(service_file=self.service_file_path)

    def open_spreadsheet(self, spreadsheet_id: str):
        self.sheet = self.__oauth.open_by_key(spreadsheet_id)

    def get_spreadsheet(self):
        self.__spreadsheet_connection_check()
        sheet = self.sheet.sheet1
        self.sheet_data = sheet.get_as_df()
