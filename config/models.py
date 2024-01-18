from dataclasses import dataclass


@dataclass
class User:
    login: str
    password: str
    api: str


@dataclass
class Api:
    name: str
    url: str

@dataclass
class Project:
    projectname: str
    api: str
    catalog_id: str

@dataclass
class ProjectData:
    catalog_id: str
    category_id: list[dict] | None


@dataclass
class Postgres:
    host: str
    port: str
    database: str
    user: str
    password: str


@dataclass
class SeoTagPageColumns:
    setting_id: str | None = None

