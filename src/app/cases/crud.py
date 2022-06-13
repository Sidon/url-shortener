import time

from sqlalchemy.orm import Session

from src.app import schemas
from src.cross import except_raise, keygen
from src.infra.db import models


def create_url(database: Session, target_url: str, custom_alias) -> models.URL:
    start = time.time()
    if custom_alias:
        if not database.query(models.URL).filter(models.URL.alias == custom_alias).first():
            alias = custom_alias
        else:
            message = dict(alias=custom_alias, error_code="001", description="CUSTOM ALIAS ALREADY EXISTS")
            except_raise.raise_bad_request(message=message)
    else:
        alias = keygen.create_unique_random_key(database)

    db_url = models.URL(target_url=target_url, alias=alias)
    database.add(db_url)
    database.commit()
    return dict(
        alias=db_url.alias,
        url=db_url.get_sortened_url(),
        statistics=dict(time_taken=f"{(time.time()-start)*1000:.5f}ms"),
    )


def get_url_from_alias(database: Session, alias: str) -> models.URL:
    return database.query(models.URL).filter(models.URL.alias == alias).first()


def get_target_url_from_db(database: Session, shortened_url: str) -> models.URL:
    _alias = shortened_url.split("/")[-1]
    response = None
    if url_from_db := get_url_from_alias(database=database, alias=_alias):
        response = url_from_db.target_url

    return response
