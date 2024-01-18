from config.config import DataManager
from db.postgres import Postgres
from config.logger import logger, log_func_calls
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

class Bitrix:

    def __init__(self):
        logger.info("Starting Bitrix")
        self.__get_user_data()
        self.database = Postgres()
        self.database()

        self.options = Options()
        self.options.add_argument(
            "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
        )

    def __call__(self, project: str):
        self.driver: webdriver = webdriver.Chrome(self.options)
        self.driver.set_window_size(1920, 1080)
        self.driver.implicitly_wait(10)
        self.__load_project_enter_url(project)
        self.properties_db = self.database.load_table_from_db_as_dict(f"properties_{project}")
        self.sections = self.database.load_table_from_db_as_dict(
            f"Sections_iPort"
        )
        self.__enter_bitrix()

    def __get_user_data(self):
        data_manager: DataManager = DataManager.get_instance()
        self.user = data_manager._DataManager__bitrix_user.login
        self.password = data_manager._DataManager__bitrix_user.password

    @log_func_calls
    def __load_project_enter_url(self, project):
        self.sites = self.database.load_table_from_db_as_dict("Sites")

        for project_data in self.sites:
            if project_data["Site"] == project:
                self.api_url = project_data["Api"]
                self.catalog_id = project_data["CatalogID"]
                self.checkbox_id = f'SITE_ID_s{project_data["ID"]}'

    @log_func_calls
    def apply_changes(self):
        self.driver.find_element(By.NAME, "apply").click()
        time.sleep(2)

    @log_func_calls
    def save_changes(self):
        self.driver.find_element(By.NAME, "save").click()
        time.sleep(2)

    @log_func_calls
    def __enter_bitrix(self):
        self.driver.get(self.api_url)
        remember_button_xpath = (
            f'//label[@for="USER_REMEMBER" and @class="adm-designed-checkbox-label"]'
        )
        remember_button = self.driver.find_element(By.XPATH, remember_button_xpath)
        login_input = self.driver.find_element(By.NAME, "USER_LOGIN")
        password_input = self.driver.find_element(By.NAME, "USER_PASSWORD")
        enter_button = self.driver.find_element(By.NAME, "Login")

        remember_button.click()
        login_input.send_keys(self.user)
        password_input.send_keys(self.password)
        enter_button.click()

        time.sleep(3)

