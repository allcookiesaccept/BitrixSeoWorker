import pandas as pd
from seo_module import SeoModule
from link_rules import rules


class LinkBuilder(SeoModule):

    def __init__(self):
        super().__init__()
        self.rules = rules
        self.fields = ['top', 'bottom']

    def _load_seo_linking_settings(self, filename: str):

        self.uploaded_settings = pd.read_excel(f'linking_rules/{filename}', dtype={'values': str})
        self._reformat_uploaded_settings_to_dict()

        return self.uploaded_settings

    def _reformat_uploaded_settings_to_dict(self):

        self.seo_settings = self.uploaded_settings.to_dict('records')
        for item in self.seo_settings:
            values = [x.lower() for x in str(item['values']).split(';')]
            keys = [x.lower() for x in str(item['keys']).split('|')]
            item['properties'] = {}
            for x, key in enumerate(keys):
                item['properties'][key] = values[x]

        return self.seo_settings

    def _link_list_variable_initiator(self):
        self.setting_top_links_list = []
        self.setting_bottom_links_list = []

        return self.setting_bottom_links_list, self.setting_top_links_list

    def _add_links_lists_to_settings_dict(self, item):
        item['top-links'] = self.setting_top_links_list
        item['bottom-links'] = self.setting_bottom_links_list

    def generate_links_for_settings(self, file, folder, project):

        self._load_seo_linking_settings(file)

        for item in self.seo_settings:
            setting_id = item['id']
            name = item['tag']
            brand = item['brand']
            key = item['keys']
            properties = item['properties']
            self._link_list_variable_initiator()
            for field in self.fields:
                self.setting_criteries = self.rules[project][folder][field][key]
                self.field = field
                self.find_links(setting_id, brand, properties)
            self._add_links_lists_to_settings_dict(item)
            self._print_added_links(name)

    def _append_setting_id_to_proper_list(self, identifier):
        match self.field:
            case 'top':
                self.setting_top_links_list.append(identifier)
            case 'bottom':
                self.setting_bottom_links_list.append(identifier)

    def find_links(self, setting_id, brand, properties):

        for criteria, property in self.setting_criteries.items():
            if property == '':
                self._get_links_by_empty_criteria(setting_id, criteria, brand)
            elif '%' in property:
                prop_key = property.split('%')[1]
                func_type = property.split('%')[0]
                prop_value = properties[prop_key]
                match func_type:
                    case 'brandless':
                        self._get_brandless_links_complex_rule(setting_id, criteria, prop_key, prop_value)
                    case 'find':
                        self._get_links_by_finding_substring(setting_id, criteria, compared_value=prop_value, search_substring=prop_key)
            elif property == 'brandless':
                self._get_brandless_links_simple_rule(setting_id, criteria)
            else:
                prop_value = properties[property]
                self._get_links_by_criteria(setting_id, criteria, brand, property, prop_value)

    def _get_links_by_finding_substring(self, setting_id, criteria, compared_value, search_substring):

        for item in self.seo_settings:
            if item['keys'] == criteria and item['id'] != setting_id and str(item['properties'][compared_value]).find(search_substring) > -1:
                identifier = item['id']
                self._append_setting_id_to_proper_list(identifier)
                

    def _print_added_links(self, name, added_top_settings_string='', added_bottom_settings_string=''):

        for setting in self.setting_top_links_list:
            for item in self.seo_settings:
                if item['id'] == setting:
                    added_top_settings_string += f'{item["tag"]}/'

        for setting in self.setting_bottom_links_list:
            for item in self.seo_settings:
                if item['id'] == setting:
                    added_bottom_settings_string += f'{item["tag"]}/'

        print(f'________________\n{name}')
        print(f'Top: {len(self.setting_top_links_list)} links: {added_top_settings_string}')
        print(f'Bot: {len(self.setting_bottom_links_list)} links: {added_bottom_settings_string}')
        print(f'________________')

    def _get_brandless_links_complex_rule(self, setting_id, criteria, property, property_value):

        for item in self.seo_settings:
            if item['keys'] == criteria and item['id'] != setting_id and item['properties'][property] == property_value:
                identifier = item['id']
                self._append_setting_id_to_proper_list(identifier)

    def _get_brandless_links_simple_rule(self, setting_id, criteria):

        for item in self.seo_settings:
            if item['keys'] == criteria and item['id'] != setting_id:
                identifier = item['id']
                self._append_setting_id_to_proper_list(identifier)

    def _get_links_by_empty_criteria(self, setting_id, criteria, brand):

        for item in self.seo_settings:
            if item['keys'] == criteria and brand == '--' and item['id'] != setting_id:
                identifier = item['id']
                self._append_setting_id_to_proper_list(identifier)
            elif item['keys'] == criteria and brand == item['brand'] and item['id'] != setting_id:
                identifier = item['id']
                self._append_setting_id_to_proper_list(identifier)

    def _get_links_by_criteria(self, setting_id, criteria, brand, property, prop_value):

        for item in self.seo_settings:
            if item['keys'] == criteria and brand == '--' and item['id'] != setting_id and item['properties'][
                property] == prop_value:
                identifier = item['id']
                self._append_setting_id_to_proper_list(identifier)
            elif item['keys'] == criteria and brand == item['brand'] and item['id'] != setting_id and item['properties'][
                property] == prop_value:
                identifier = item['id']
                self._append_setting_id_to_proper_list(identifier)

    def fill_linking_fields_in_bitrix(self):

        for item in self.seo_settings:
            self.setting_top_links = ','.join(str(x) for x in item['top-links'])
            self.setting_bottom_links = ','.join(str(x) for x in item['bottom-links'])
            self.setting_id = item['id']
            self.driver.get(f'{self.edit_setting_url}{self.setting_id}')
            self._add_setting_top_links()
            self._add_setting_bottom_links()
            self._apply_changes()


def main():

    lb = LinkBuilder()
    lb._load_seo_linking_settings('monitors.xlsx')

if __name__ == '__main__':
    main()
