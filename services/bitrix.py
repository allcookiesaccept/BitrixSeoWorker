from config.models import User
from config.logger import logger, log_func_calls
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

class Bitrix:

    SITES_VALUES ={
        "site_1": {"catalog_id": "5", "checkbox": "SITE_ID_s1"},
        "site_2": {"catalog_id": "59", "checkbox": "SITE_ID_s4"},
        "site_3": {"catalog_id": "25", "checkbox": "SITE_ID_s2"},
        "site_4": {"catalog_id": "62", "checkbox": "SITE_ID_s6"},
    }

    def __init__(self, bitrix_user: User):
        logger.info("Starting Bitrix")
        self.options = Options()
        self.options.add_argument(
            "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
        )
        self.bitrix_user = bitrix_user
        self.driver: webdriver = webdriver.Chrome(self.options)
        self.driver.set_window_size(1920, 1080)
        self.driver.implicitly_wait(10)


    def __call__(self, site: str):
        self.__load_project_enter_url(site)
        self.__enter_bitrix(site)

    @log_func_calls
    def __enter_bitrix(self, site: str):
        self.driver.get(self.api_url)
        remember_button_xpath = (
            f'//label[@for="USER_REMEMBER" and @class="adm-designed-checkbox-label"]'
        )
        remember_button = self.driver.find_element(By.XPATH, remember_button_xpath)
        login_input = self.driver.find_element(By.NAME, "USER_LOGIN")
        password_input = self.driver.find_element(By.NAME, "USER_PASSWORD")
        enter_button = self.driver.find_element(By.NAME, "Login")

        remember_button.click()
        login_input.send_keys(self.bitrix_user.login)
        password_input.send_keys(self.bitrix_user.password)
        enter_button.click()

        time.sleep(3)

    @log_func_calls
    def __load_project_enter_url(self, project):

        match project:
            case site if site == "site_1":
                self.api_url = self.bitrix_user.api_urls["site_1"]
                self.catalog_id = Bitrix.SITES_VALUES["site_1"]["catalog_id"]
                self.checkbox_id = Bitrix.SITES_VALUES["site_1"]["checkbox"]
            case site if site == "site_2":
                self.api_url = self.bitrix_user.api_urls["site_2"]
                self.catalog_id = Bitrix.SITES_VALUES["site_2"]["catalog_id"]
                self.checkbox_id = Bitrix.SITES_VALUES["site_2"]["checkbox"]
            case site if site == "site_3":
                self.api_url = self.bitrix_user.api_urls["site_3"]
                self.catalog_id = Bitrix.SITES_VALUES["site_3"]["catalog_id"]
                self.checkbox_id = Bitrix.SITES_VALUES["site_3"]["checkbox"]
            case site if site == "site_4":
                self.api_url = self.bitrix_user.api_urls["site_4"]
                self.catalog_id = Bitrix.SITES_VALUES["site_4"]["catalog_id"]
                self.checkbox_id = Bitrix.SITES_VALUES["site_4"]["checkbox"]

    def apply_changes(self):
        self.driver.find_element(By.NAME, "apply").click()
        time.sleep(2)

    def save_changes(self):
        self.driver.find_element(By.NAME, "save").click()
        time.sleep(2)



