from db.postgres import Postgres
import pandas as pd



class SeoModuleDBCreator:

    def __init__(self):
        self.id_col = '\"ID\"', "SERIAL PRIMARY KEY"
        self.postgres = Postgres()
        self.postgres()
        super().__init__()
        self.__init_sites_columns()
        self.__init_properties_columns()
        self.__init_sections_columns()

    def __check__tables(self):
        ...

    def __call__(self, project: str = 'iport'):
        self.project = project
        self.postgres.create_table('sites', self.tableSites)
        self.postgres.create_table(f'{project}_sections', self.tableSections)
        self.postgres.create_table(f'{project}_properties', )

    def __init_sites_columns(self):

        site_name_col = '\"Site\"', "VARCHAR(255) NOT NULL"
        api_col = '\"Api\"', "VARCHAR(255) NOT NULL"
        catalog_id_col = '\"CatalogID\"', "VARCHAR(255) NOT NULL"
        self.tableSites = [self.id_col, site_name_col, api_col, catalog_id_col]


    def __init_properties_columns(self):
        property_name = '\"PropertyName\"', "VARCHAR(128) NOT NULL"
        property_value = '\"PropertyValue\"', "VARCHAR(128) NOT NULL"
        property_key = '\"PropertyKey\"', "VARCHAR(16) NOT NULL"
        key_value_id = '\"KeyValueID\"', "VARCHAR(255) NOT NULL"
        property_type = '\"PropertyType\"', "VARCHAR(16) NOT NULL"

        self.tableProperties = [self.id_col, property_name, property_value, property_key, key_value_id, property_type]


    def __init_sections_columns(self):

        section_name = '\"SectionName\"', "VARCHAR(64) NOT NULL"
        level = '\"Level\"', "VARCHAR(8) NULL"
        parent = '\"Parent\"', "VARCHAR(64) NOT NULL"
        slug = '\"Slug\"', "VARCHAR(255) NOT NULL"
        section_id = '\"SectionID\"', "VARCHAR(8) NOT NULL"
        self.tableSections = [self.id_col, section_name, level, parent, slug, section_id]


    def __get_dict_from_file(self, file_path: str):

        values = pd.read_excel(file_path)
        return values.to_dict('records')


