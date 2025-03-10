import pygsheets
from pathlib import Path
from config.logger import logger


class GoogleSheet:
    def __init__(self, service_file_path: str = service_file_path):
        logger.info("Starting GoogleSheet")
        self.service_file_path = service_file_path

    def __call__(self, spreadsheet_id: str):
        self.__oauth()
        self.open_spreadsheet(spreadsheet_id)
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
        self.all_values = sheet.get_all_values()
        self.values = sheet.get_values()

    def get_pandas_df_from_spreadsheet(self) -> pandas.DataFrame:
        headers = self.sheet_data.pop(0)
        df = pd.DataFrame(self.sheet_data, columns=headers)
        df.dropna()
        return df
