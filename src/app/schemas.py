import validators
from pydantic import BaseModel, ValidationError, validator


class URL(BaseModel):
    alias: str
    url: str

    @validator("url")
    def validate_url(cls, value):
        if not validators.url(value):
            raise_bad_request(message="Your provided URL is not valid")
        return value
