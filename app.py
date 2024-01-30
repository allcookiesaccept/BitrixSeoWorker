from seo.module.tag_page_editor import TagPageEditor
from services.bitrix import Bitrix
from config.logger import logger
from config.config import DataManager
from services.google_sheets import GoogleSheet


class Worker:
    def __init__(self):
        logger.info("Starting Worker")
        data_manager = DataManager().get_instance()
        self.google_sheet = data_manager.google_sheets
        self.bitrix_user = data_manager.bitrix_user

    def __call__(self, site: str = "site_1"):
        self.settings_list = self.load_settings()
        self.session = Bitrix(self.bitrix_user)
        self.session(site)
        self.editor = TagPageEditor(self.session)

    def load_settings(self, file_path: str = None, spread_sheet_id: str = None):
        filepath = file_path or self.google_sheet.service_file_path
        spreadsheetID = spread_sheet_id or self.google_sheet.spread_sheet_id
        sheet_worker = GoogleSheet(filepath, spreadsheetID)
        settings_df = sheet_worker.sheet_data
        return settings_df.to_dict("records")

    def update_seo_module_pages(self):
        for setting in self.settings_list:
            if type(setting) == dict:
                self.editor(setting)
