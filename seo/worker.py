from seo.settings_loader import SettingsLoader
from seo.module.tag_page_editor import TagPageEditor
from seo.module.tag_page_parser import TagPageParser
from services.bitrix import Bitrix
from config.logger import logger



class Worker:
    def __init__(self):
        logger.info("Starting Worker")
        self.settings = SettingsLoader()
        self.settings_list = self.settings().to_dict('records')
        self.session = None
        self.editor = None
        self.parser = None

    def __call__(self, api):
        self.session = Bitrix()
        self.session(api)  #

    def run_editor(self):
        if not self.session:
            raise Exception("Сессия Bitrix не инициализирована. Сначала вызовите worker(api).")
        self.editor = TagPageEditor(self.session)
        self.update_seo_module_pages()

    def run_parser(self):
        if not self.session:
            raise Exception("Сессия Bitrix не инициализирована. Сначала вызовите worker(api).")
        self.parser = TagPageParser(self.session)
        self.parser()

    def update_seo_module_pages(self):
        for setting in self.settings_list:
            if isinstance(setting, dict):
                self.editor(setting)