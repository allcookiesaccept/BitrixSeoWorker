from services.bitrix import Bitrix
from seo.module.tag_page_editor_methods import TagPageEditorMethods
from config.logger import logger, log_func_calls
import time


class TagPageEditor(TagPageEditorMethods):
    @log_func_calls
    def __init__(self, session: Bitrix):
        logger.info("Starting TagPageEditor")
        super().__init__(session)
        self.session: Bitrix = session

    @log_func_calls
    def __call__(self, page_data: dict):
        self.page_data = page_data
        self.__form_session_url()
        self.session.driver.get(self.session_url)
        self.__proccess_page_data()
        self.session.apply_changes()

    @log_func_calls
    def __proccess_page_data(self):
        match self.page_data["type"]:
            case "new":
                self.__create_new_page()
            case "update":
                self.__update_page_info()
            case "deactivate":
                self._click_on_activity_checkbox()

    @log_func_calls
    def __create_new_page(self):
        self._click_site_checkbox()
        self.__update_page_info()

    @log_func_calls
    def __update_page_info(self):
        exclude = ["type", "id", "api_url", "section"]

        for key, value in self.page_data.items():
            if key not in exclude and value != "":
                function = self.dict_of_methods[key]
                function(value)
                time.sleep(1)

    @log_func_calls
    def __form_session_url(self):
        edit_slug = "zverushki.seofilter_setting_edit.php?ID="
        new_slug = "zverushki.seofilter_setting_edit.php?lang=ru&IBLOCK_ID="
        page_type = self.page_data["type"]

        if page_type == "update" or page_type == "deactivate":
            self.session_url = (
                f'{self.session.api_url}{edit_slug}{self.page_data["id"]}'
            )

        if page_type == "new":
            try:
                for section in self.session.sections:
                    if (
                        str(section["SectionName"]).lower()
                        == str(self.page_data["section"]).lower()
                    ):
                        section_id = section["SectionID"]
                        self.session_url = f"{self.session.api_url}{new_slug}{self.session.catalog_id}&SECTION_ID={section_id}"
            except Exception as e:
                print(e)
