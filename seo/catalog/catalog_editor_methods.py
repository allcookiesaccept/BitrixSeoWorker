






def fill_1c_catalog_values(self, filename):
    self.added_settings = 0

    self._load_seo_settings(filename)
    self._count_settings()

    for setting in self.seo_settings:
        try:
            print(f"Filling {self.catalog_folder_id} category")
            self._open_1c_catalog_page()
            self._click_seo_tab()
            self._fill_catalog_folder_title()
            self._fill_catalog_folder_description()
            self._fill_catalog_folder_header()
            self._fill_catalog_product_title()
            self._fill_catalog_product_description()
            self._fill_catalog_product_header()
            self._apply_changes()
            self._added_settings_counter()
        except Exception as ex:
            print(f"{self.catalog_folder_id}: {ex}")


def _open_1c_catalog_page(self):
    self.driver.get(self.catalog_edit_page)
    time.sleep(3)


def _click_seo_tab(self):
    seo_tab_id = "tab_cont_edit5"
    tab = self.driver.find_element(By.XPATH, f'//span[@id="{seo_tab_id}"]')
    tab.click()


def _fill_catalog_folder_title(self):
    title_checkbox = f'//label[@for="ck_IPROPERTY_TEMPLATES_SECTION_META_TITLE"]'
    title_checkbox_field = self.driver.find_element(By.XPATH, title_checkbox)
    self.driver.execute_script(
        "arguments[0].scrollIntoView({'block':'center','inline':'center'});",
        title_checkbox_field,
    )
    title_checkbox_field.click()

    title_input = '//textarea[@id="IPROPERTY_TEMPLATES_SECTION_META_TITLE"]'
    title_field = self.driver.find_element(By.XPATH, title_input)
    title_field.clear()
    title_field.send_keys(self.catalog_folder_title)


def _fill_catalog_folder_description(self):
    description_checkbox = (
        f'//label[@for="ck_IPROPERTY_TEMPLATES_SECTION_META_DESCRIPTION"]'
    )
    description_checkbox_field = self.driver.find_element(
        By.XPATH, description_checkbox
    )
    self.driver.execute_script(
        "arguments[0].scrollIntoView({'block':'center','inline':'center'});",
        description_checkbox_field,
    )
    description_checkbox_field.click()

    description_input = '//textarea[@id="IPROPERTY_TEMPLATES_SECTION_META_DESCRIPTION"]'
    description_field = self.driver.find_element(By.XPATH, description_input)
    description_field.clear()
    description_field.send_keys(self.catalog_folder_description)


def _fill_catalog_folder_header(self):
    header_checkbox = f'//label[@for="ck_IPROPERTY_TEMPLATES_SECTION_PAGE_TITLE"]'
    header_checkbox_field = self.driver.find_element(By.XPATH, header_checkbox)
    self.driver.execute_script(
        "arguments[0].scrollIntoView({'block':'center','inline':'center'});",
        header_checkbox_field,
    )
    header_checkbox_field.click()

    header_input = '//textarea[@id="IPROPERTY_TEMPLATES_SECTION_PAGE_TITLE"]'
    header_field = self.driver.find_element(By.XPATH, header_input)
    header_field.clear()
    header_field.send_keys("{=this.Name}")


def _fill_catalog_product_title(self):
    title_checkbox = f'//label[@for="ck_IPROPERTY_TEMPLATES_ELEMENT_META_TITLE"]'
    title_checkbox_field = self.driver.find_element(By.XPATH, title_checkbox)
    self.driver.execute_script(
        "arguments[0].scrollIntoView({'block':'center','inline':'center'});",
        title_checkbox_field,
    )
    title_checkbox_field.click()

    title_input = '//textarea[@id="IPROPERTY_TEMPLATES_ELEMENT_META_TITLE"]'
    title_field = self.driver.find_element(By.XPATH, title_input)
    title_field.clear()
    title_field.send_keys(self.catalog_product_title)


def _fill_catalog_product_description(self):
    description_checkbox = (
        f'//label[@for="ck_IPROPERTY_TEMPLATES_ELEMENT_META_DESCRIPTION"]'
    )
    description_checkbox_field = self.driver.find_element(
        By.XPATH, description_checkbox
    )
    self.driver.execute_script(
        "arguments[0].scrollIntoView({'block':'center','inline':'center'});",
        description_checkbox_field,
    )
    description_checkbox_field.click()

    description_input = '//textarea[@id="IPROPERTY_TEMPLATES_ELEMENT_META_DESCRIPTION"]'
    description_field = self.driver.find_element(By.XPATH, description_input)
    description_field.clear()
    description_field.send_keys(self.catalog_product_description)


def _fill_catalog_product_header(self):
    header_checkbox = f'//label[@for="ck_IPROPERTY_TEMPLATES_ELEMENT_PAGE_TITLE"]'
    header_checkbox_field = self.driver.find_element(By.XPATH, header_checkbox)
    self.driver.execute_script(
        "arguments[0].scrollIntoView({'block':'center','inline':'center'});",
        header_checkbox_field,
    )
    header_checkbox_field.click()

    header_input = '//textarea[@id="IPROPERTY_TEMPLATES_ELEMENT_PAGE_TITLE"]'
    header_field = self.driver.find_element(By.XPATH, header_input)
    header_field.clear()
    header_field.send_keys("{=this.Name}")


def _click_property_tab(self):
    prop_tab_id = "tab_cont_edit4"
    tab = self.driver.find_element(By.XPATH, f'//span[@id="{prop_tab_id}"]')
    tab.click()


def _click_links_list_tab(self):
    list_tab = "tab_cont_edit2"
    tab = self.driver.find_element(By.XPATH, f'//span[@id="{list_tab}"]')
    tab.click()


def _show_all_links_on_page(self):
    links_on_page_selector = Select(
        self.driver.find_element(By.XPATH, '//select[@class="adm-select"]')
    )
    links_on_page_selector.select_by_value("0")


def _scrape_links_from_setting_table(self):
    links_table_xpath = (
        '//div[@class="adm-list-table-wrap adm-list-table-without-footer"]//table[@class="adm-list-table"]'
        '//tbody//tr[@class="adm-list-table-row"]//td[2]'
    )
    table_links = self.driver.find_elements(By.XPATH, links_table_xpath)
    self.table_links = [x.text for x in table_links]

    return self.table_links


def add_properties_to_group(self, props, edit_page, tab_id_properties):
    for row in props:
        url = f'{edit_page}{row["folder_code"]}'
        folder_properties = row["prop_names"].split(",")
        self.driver.get(url)
        self.driver.find_element(By.ID, tab_id_properties).click()
        for property in folder_properties:
            options_list = self.driver.find_elements(
                By.XPATH, f'//select[@id="select_SECTION_PROPERTY"]//option'
            )
            add_button = self.driver.find_element(
                By.XPATH, f'//input[@value="Добавить"]'
            )
            for option in options_list:
                if option.text.find(f"{property}]") == 1:
                    option.click()
                    self.driver.execute_script(
                        "arguments[0].scrollIntoView({'block':'center','inline':'center'});",
                        add_button,
                    )
                    add_button.click()
                else:
                    pass

        self._apply_changes()
