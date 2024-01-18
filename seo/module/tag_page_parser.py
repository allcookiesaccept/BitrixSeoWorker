from services.bitrix import Bitrix
from config.logger import logger
from bs4 import BeautifulSoup

class TagPageParser:

    TOTAL_PAGES_LIST = 'zverushki.seofilter_settings.php?SIZEN_1=5000&filter_site_id='

    def __init__(self, session: Bitrix):
        logger.info("Starting TagPageParser")
        self.session: Bitrix = session
        self.chosen_properties_string = f'input.adm-designed-checkbox[checked="checked"]'


    def __call__(self):

        # open pages - total or segmented
        self.session.driver.get(f'{self.session.api_url}{TagPageParser.TOTAL_PAGES_LIST}{self.session.checkbox_id.split("_")[-1]}')

        page_source = self.session.driver.page_source
        soup = BeautifulSoup(page_source, 'html.parser')
        tags_table = soup.find('table', class_='adm-list-table')
        tags_list = tags_table.find('tbody')
        links = []
        rows = tags_list.find_all('tr')
        first_separator = "Изменить текущую настройку','ONCLICK':'BX.adminPanel.Redirect([], \\'"
        second_separator = '&lang'
        for row in rows:
            html_attribute: str = row.get('oncontextmenu')
            path = html_attribute.split(first_separator)[1].split(second_separator)[0]
            link = f"{self.session.api_url}{path}"
            links.append(link)


    def __parse_page(self):
        page_source = self.session.driver.page_source
        soup = BeautifulSoup(page_source, 'html.parser')
        section_selector = soup.find('select', attrs={'name': 'SECTION_ID'})
        selected_option = section_selector.select_one('option[selected]')
        section_id = selected_option.get('value')
        zver_block = soup.find('div', class_='zver-filter')
