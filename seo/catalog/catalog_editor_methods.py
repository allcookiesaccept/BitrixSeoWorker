from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from config.logger import logger

# update
class CatalogEditorMethods:
    def __init__(self, session):
        logger.info("Starting TagPageEditorMethods")
        self.session = session
        self.__init_dict_of_methods()

    def __init_dict_of_methods(self):
        self.catalog_of_methods = {
            "catalog_title": self.__add_cluster_name,
            "catalog_description": self.__add_url,
            "catalog_header": self.__add_product_tag_name,
            "product_title": self.__add_catalog_tag_name,
            "product_description": self.__add_header,
            "product_header": self.__add_meta_title,
        }



    def _open_1c_catalog_page(self):
        ...

    def _click_seo_tab(self):
        seo_tab_id = "tab_cont_edit5"
        tab = self.session.driver.find_element(By.XPATH, f'//span[@id="{seo_tab_id}"]')
        tab.click()

    
    def _fill_catalog_folder_title(self, input_value):
        title_checkbox = f'//label[@for="ck_IPROPERTY_TEMPLATES_SECTION_META_TITLE"]'
        title_checkbox_field = self.session.driver.find_element(By.XPATH, title_checkbox)
        self.session.driver.execute_script(
            "arguments[0].scrollIntoView({'block':'center','inline':'center'});",
            title_checkbox_field,
        )
        title_checkbox_field.click()
    
        title_input = '//textarea[@id="IPROPERTY_TEMPLATES_SECTION_META_TITLE"]'
        title_field = self.session.driver.find_element(By.XPATH, title_input)
        title_field.clear()
        title_field.send_keys(self.catalog_folder_title)
    
    
    def _fill_catalog_folder_description(self, input_value):
        description_checkbox = (
            f'//label[@for="ck_IPROPERTY_TEMPLATES_SECTION_META_DESCRIPTION"]'
        )
        description_checkbox_field = self.session.driver.find_element(
            By.XPATH, description_checkbox
        )
        self.session.driver.execute_script(
            "arguments[0].scrollIntoView({'block':'center','inline':'center'});",
            description_checkbox_field,
        )
        description_checkbox_field.click()
    
        description_input = '//textarea[@id="IPROPERTY_TEMPLATES_SECTION_META_DESCRIPTION"]'
        description_field = self.session.driver.find_element(By.XPATH, description_input)
        description_field.clear()
        description_field.send_keys(self.catalog_folder_description)
    
    
    def _fill_catalog_folder_header(self, input_value):
        header_checkbox = f'//label[@for="ck_IPROPERTY_TEMPLATES_SECTION_PAGE_TITLE"]'
        header_checkbox_field = self.session.driver.find_element(By.XPATH, header_checkbox)
        self.session.driver.execute_script(
            "arguments[0].scrollIntoView({'block':'center','inline':'center'});",
            header_checkbox_field,
        )
        header_checkbox_field.click()
    
        header_input = '//textarea[@id="IPROPERTY_TEMPLATES_SECTION_PAGE_TITLE"]'
        header_field = self.session.driver.find_element(By.XPATH, header_input)
        header_field.clear()
        header_field.send_keys("{=this.Name}")
    
    
    def _fill_catalog_product_title(self, input_value):
        title_checkbox = f'//label[@for="ck_IPROPERTY_TEMPLATES_ELEMENT_META_TITLE"]'
        title_checkbox_field = self.session.driver.find_element(By.XPATH, title_checkbox)
        self.session.driver.execute_script(
            "arguments[0].scrollIntoView({'block':'center','inline':'center'});",
            title_checkbox_field,
        )
        title_checkbox_field.click()
    
        title_input = '//textarea[@id="IPROPERTY_TEMPLATES_ELEMENT_META_TITLE"]'
        title_field = self.session.driver.find_element(By.XPATH, title_input)
        title_field.clear()
        title_field.send_keys(self.catalog_product_title)
    
    
    def _fill_catalog_product_description(self, input_value):
        description_checkbox = (
            f'//label[@for="ck_IPROPERTY_TEMPLATES_ELEMENT_META_DESCRIPTION"]'
        )
        description_checkbox_field = self.session.driver.find_element(
            By.XPATH, description_checkbox
        )
        self.session.driver.execute_script(
            "arguments[0].scrollIntoView({'block':'center','inline':'center'});",
            description_checkbox_field,
        )
        description_checkbox_field.click()
    
        description_input = '//textarea[@id="IPROPERTY_TEMPLATES_ELEMENT_META_DESCRIPTION"]'
        description_field = self.session.driver.find_element(By.XPATH, description_input)
        description_field.clear()
        description_field.send_keys(self.catalog_product_description)
    
    
    def _fill_catalog_product_header(self, input_value):
        header_checkbox = f'//label[@for="ck_IPROPERTY_TEMPLATES_ELEMENT_PAGE_TITLE"]'
        header_checkbox_field = self.session.driver.find_element(By.XPATH, header_checkbox)
        self.session.driver.execute_script(
            "arguments[0].scrollIntoView({'block':'center','inline':'center'});",
            header_checkbox_field,
        )
        header_checkbox_field.click()
    
        header_input = '//textarea[@id="IPROPERTY_TEMPLATES_ELEMENT_PAGE_TITLE"]'
        header_field = self.session.driver.find_element(By.XPATH, header_input)
        header_field.clear()
        header_field.send_keys("{=this.Name}")
    
    
    def _click_property_tab(self):
        prop_tab_id = "tab_cont_edit4"
        tab = self.session.driver.find_element(By.XPATH, f'//span[@id="{prop_tab_id}"]')
        tab.click()
    
    
    def _click_links_list_tab(self):
        list_tab = "tab_cont_edit2"
        tab = self.session.driver.find_element(By.XPATH, f'//span[@id="{list_tab}"]')
        tab.click()
    
    
    def _show_all_links_on_page(self):
        links_on_page_selector = Select(
            self.session.driver.find_element(By.XPATH, '//select[@class="adm-select"]')
        )
        links_on_page_selector.select_by_value("0")
    
    
    def _scrape_links_from_setting_table(self):
        links_table_xpath = (
            '//div[@class="adm-list-table-wrap adm-list-table-without-footer"]//table[@class="adm-list-table"]'
            '//tbody//tr[@class="adm-list-table-row"]//td[2]'
        )
        table_links = self.session.driver.find_elements(By.XPATH, links_table_xpath)
        self.table_links = [x.text for x in table_links]
    
        return self.table_links


    def add_properties_to_group(self, props, edit_page, tab_id_properties):
        for row in props:
            url = f'{edit_page}{row["folder_code"]}'
            folder_properties = row["prop_names"].split(",")
            self.session.driver.get(url)
            self.session.driver.find_element(By.ID, tab_id_properties).click()
            for property in folder_properties:
                options_list = self.session.driver.find_elements(
                    By.XPATH, f'//select[@id="select_SECTION_PROPERTY"]//option'
                )
                add_button = self.session.driver.find_element(
                    By.XPATH, f'//input[@value="Добавить"]'
                )
                for option in options_list:
                    if option.text.find(f"{property}]") == 1:
                        option.click()
                        self.session.driver.execute_script(
                            "arguments[0].scrollIntoView({'block':'center','inline':'center'});",
                            add_button,
                        )
                        add_button.click()
                    else:
                        pass
    
            self._apply_changes()
