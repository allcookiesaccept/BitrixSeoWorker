from selenium.webdriver.common.by import By
from config.logger import logger, log_func_calls


class TagPageEditorMethods:
    def __init__(self, session):
        logger.info("Starting TagPageEditorMethods")
        self.session = session
        self.__init__dict_of_methods()

    def __init__dict_of_methods(self) -> None:
        self.dict_of_methods = {
            "cluster": self.__add_cluster_name,
            "link": self.__add_url,
            "product_name": self.__add_product_tag_name,
            "tag_name": self.__add_catalog_tag_name,
            "header": self.__add_header,
            "meta_title": self.__add_meta_title,
            "meta_description": self.__add_meta_description,
            "top_linking": self.__add_top_linking,
            "bottom_linking": self.__add_bottom_linking,
            "properties": self.__process_properties,
        }

    # update
    def __add_product_tag_name(self, input_value: str) -> None:
        tag_input = self.session.driver.find_element(By.NAME, "TAG_NAME")
        tag_input.clear()
        tag_input.send_keys(input_value)

    def __add_catalog_tag_name(self, input_value: str) -> None:
        tag_input = self.session.driver.find_element(By.NAME, "TAG_SECTION_NAME")
        tag_input.clear()
        tag_input.send_keys(input_value)

    def __add_header(self, input_value: str) -> None:
        header = self.session.driver.find_element(By.NAME, "PAGE_TITLE")
        header.clear()
        header.send_keys(input_value)

    def __add_cluster_name(self, input_value: str) -> None:
        description = self.session.driver.find_element(By.NAME, "DESCRIPTION")
        description.clear()
        description.send_keys(input_value)

    def __add_url(self, input_value: str) -> None:
        url_field = self.session.driver.find_element(By.NAME, "URL_CPU")
        url_field.clear()
        url_field.send_keys(input_value.lower())

    def __add_meta_title(self, input_value: str) -> None:
        meta_title_input = self.session.driver.find_element(By.NAME, "META_TITLE")
        meta_title_input.clear()
        meta_title_input.send_keys(input_value)

    def __add_top_linking(self, input_value: str) -> None:
        top_links = self.session.driver.find_element(By.NAME, "RELATED_SETTING_ID")
        self.session.driver.execute_script(
            "arguments[0].scrollIntoView({'block':'center','inline':'center'});",
            top_links,
        )
        top_links.clear()
        top_links.send_keys(input_value)

    def __add_meta_description(self, input_value: str) -> None:
        meta_description_input = self.session.driver.find_element(
            By.NAME, "META_DESCRIPTION"
        )
        meta_description_input.clear()
        meta_description_input.send_keys(input_value)

    def __add_bottom_linking(self, input_value: str) -> None:
        bottom_links = self.session.driver.find_element(By.NAME, "RELATED_SETTING_ID2")
        self.session.driver.execute_script(
            "arguments[0].scrollIntoView({'block':'center','inline':'center'});",
            bottom_links,
        )
        bottom_links.clear()
        bottom_links.send_keys(input_value)

    def __scroll_to_property_block(self, property_name: str) -> None:
        xpath_query = f'//div[contains(text(), "{property_name}") and @class="bx-filter-parameters-box-title"]'
        property_block = self.session.driver.find_element(By.XPATH, xpath_query)
        self.session.driver.execute_script(
            "arguments[0].scrollIntoView(true);", property_block
        )

    def __generate_xpath_search_string_for_property_input_element(
        self, property_type: str, property_key: str
    ) -> str:
        search_string = None
        match property_type:
            case "checkbox":
                search_string = (
                    f'label.adm-designed-checkbox-label[for="{property_key}"]'
                )
                # TODO fix radio button selector
            case "radio":
                search_string = f'//div[@class="radio"]//label[@for="{property_key}"]//span//input[@id="{property_key}"]'

        return search_string

    def _click_site_checkbox(self) -> None:
        checkbox_xpath = f'//li//label//label[@for="{self.session.checkbox_id}"]'
        checkbox = self.session.driver.find_element(By.XPATH, checkbox_xpath)
        self.session.driver.execute_script("arguments[0].click();", checkbox)

    @log_func_calls
    def _click_on_activity_checkbox(self):
        search_string = f'label.adm-designed-checkbox-label[for="ACTIVE"]'
        activity_checkbox = self.session.driver.find_element(
            By.CSS_SELECTOR, search_string
        )
        self.session.driver.execute_script("arguments[0].click();", activity_checkbox)

    def __process_properties(self, input_value: str) -> None:
        properties = input_value.split("|")
        properties_dict = {
            prop.split(":")[0]: prop.split(":")[1] for prop in properties
        }
        for property_key, property_value in properties_dict.items():
            for property_row in self.session.properties_db:
                if (
                    property_key == property_row["PropertyKey"]
                    and str(property_value).lower()
                    == str(property_row["PropertyValue"]).lower()
                ):
                    property_type = property_row["PropertyType"]
                    property_key_value_id = property_row["KeyValueID"]
                    property_key_value_id = property_key_value_id.split("count_")[1]
                    property_name = property_row["PropertyName"]
                    self.__scroll_to_property_block(property_name)
                    element_xpath_string = (
                        self.__generate_xpath_search_string_for_property_input_element(
                            property_type, property_key_value_id
                        )
                    )
                    property_checkbox = self.session.driver.find_element(
                        By.CSS_SELECTOR, element_xpath_string
                    )
                    self.session.driver.execute_script(
                        "arguments[0].click();", property_checkbox
                    )
