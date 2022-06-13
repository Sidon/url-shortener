import types
from src.cross import data_helper
from src.infra.db import db_services


def test_get_db():
    db_services.sessionmaker= lambda autocommit=False, autoflush=False, bind='engine': 'MockDB'
    db = db_services.get_db()
    assert isinstance(db, types.GeneratorType)

def test_init_db():
    db_services.create_database= lambda database_url='f4k3_url': True
