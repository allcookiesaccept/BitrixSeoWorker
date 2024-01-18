




class SettingsCounter:
    def __init__(self):
        self.updated_pages = 0
        self.uploaded_settings = None
        self.seo_settings = None
        self.added_settings = 0

    def _count_settings(self):
        if self.seo_settings is not None:
            try:
                self.total_uploaded_settings = len(self.seo_settings)
            except Exception as e:
                print(e)

    def simple_message(self):
        self.__total_settings_counter()
        self.__added_settings_counter()

    def __total_settings_counter(self):
        print(f"Remains {self.total_uploaded_settings} pages")
        self.total_uploaded_settings -= 1

    def __added_settings_counter(self):
        self.added_settings += 1
        print(f"Finished {self.added_settings} pages")
