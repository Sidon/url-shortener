from typing import Optional

from sqlmodel import Field, SQLModel

from src.settings import BASE_URL


class URL(SQLModel, table=True):
    __tablename__ = "urls"
    id: Optional[int] = Field(default=None, primary_key=True)
    alias: str = Field(sa_column_kwargs={"unique": True}, index=True)
    target_url: str = Field(index=True)

    def get_url(self):
        return f"{BASE_URL}/u/{self.alias}"
