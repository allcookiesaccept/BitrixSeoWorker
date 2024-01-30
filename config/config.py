from config.models import User, Postgres, GoogleSheet
from dotenv import load_dotenv
import os


BASE_DIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))


class DataManager:

    __instance = None

    @staticmethod
    def get_instance():
        if DataManager.__instance is None:
            DataManager()
        return DataManager.__instance

    def __init__(self):
        if DataManager.__instance is not None:
            raise Exception("DataManger is a singleton class")
        else:
            load_dotenv()
            self.bitrix_user = self.load_bitrix_user()
            self.postgres_info = self.load_postgres_data()
            self.google_sheets = self.get_google_oauth_data()
            DataManager.__instance = self

    def load_bitrix_user(self) -> User:

        login = os.getenv("LOGIN")
        password = os.getenv("PASSWORD")
        api_urls = {
            "site_1": os.getenv("SITE_1_API"),
            "site_2": os.getenv("SITE_2_API"),
            "site_3": os.getenv("SITE_3_API"),
            "site_4": os.getenv("SITE_4_API"),
        }

        return User(login=login, password=password, api_urls=api_urls)


    def get_google_oauth_data(self):
        service_file = os.getenv("SERVICE_FILE_NAME")
        spread_sheet_id = os.getenv("SPREAD_SHEET_ID")
        return GoogleSheet(filepath=service_file, spread_sheet_id=spread_sheet_id)



    def load_postgres_data(self) -> Postgres:
        host = os.getenv("POSTGRES_HOST")
        port = os.getenv("POSTGRES_PORT")
        database = os.getenv("POSTGRES_DB")
        user = os.getenv("POSTGRES_USER")
        password = os.getenv("POSTGRES_PASSWORD")

        return Postgres(host, port, database, user, password)
