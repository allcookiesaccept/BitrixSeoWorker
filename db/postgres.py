import psycopg2
from config.config import DataManager


class Postgres:
    def __init__(self):
        data_manager: DataManager = DataManager.get_instance()
        self.host = data_manager._DataManager__postgres_info.host
        self.port = data_manager._DataManager__postgres_info.port
        self.database = data_manager._DataManager__postgres_info.database
        self.user = data_manager._DataManager__postgres_info.user
        self.password = data_manager._DataManager__postgres_info.password

    def __check_connection(self):
        if not self.connection:
            print("Not connected to the database!")
            return

    def __call__(self):
        try:
            self.connection = psycopg2.connect(
                host=self.host,
                port=self.port,
                database=self.database,
                user=self.user,
                password=self.password,
            )
            print(f"Connected to the {self.database} database")

        except Exception as e:
            print("Error connecting to the PostgreSQL database:", str(e))

    def create_database(self, database_name):
        try:
            self.__check_connection()
            cursor = self.connection.cursor()

            creation_query = f"CREATE DATABASE {database_name}"
            cursor.execute(creation_query)
            cursor.close()
            self.connection.commit()
            print(f"Database {database_name} created successfully!")
        except (Exception, psycopg2.Error) as error:
            print("Error while creating the database:", error)

    def drop_database(self, database_name):
        try:
            self.__check_connection()
            cursor = self.connection.cursor()
            drop_query = f"DROP DATABASE {database_name}"
            cursor.execute(drop_query)
            cursor.close()
            self.connection.commit()
            print(f"Database {database_name} dropped successfully!")
        except (Exception, psycopg2.Error) as error:
            print("Error while dropping the database:", error)


    def close(self):
        if self.connection:
            self.connection.close()
            print("Connection to the PostgreSQL database closed")
