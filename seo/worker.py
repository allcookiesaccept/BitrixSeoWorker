from seo.settings_loader import SettingsLoader
from seo.module.tag_page_editor import TagPageEditor
from services.bitrix import Bitrix
from config.logger import logger


class Worker:

    def __init__(self):
        data_manager = DataManager().get_instance()
        self.service_file_path = data_manager.service_file_path
        logger.info("Starting Worker")

    def load_settings(self):
        settings = SettingsLoader()
        self.settings_list = settings().to_dict('records')

    def __call__(self, api):
        self.session = Bitrix()
        self.session(api)
        self.editor = TagPageEditor(self.session)
        # self.parser = TagPageParser(self.session)

    def update_seo_module_pages(self):

        for setting in self.settings_list:
            if type(setting) == dict:
                self.editor(setting)

    def _choose_task(self):

        self.task_type = input('Choose task type (print number)\n1 - SeoModule update\n2 - Catalog update\nq - for exit')
        if self.task_type not in ['1', '2', 'q']:
            print('choose wisely, here we go again')
            self._choose_task()

