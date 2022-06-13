from typing import Optional

import validators
from fastapi import Depends, FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session

from src import settings
from src.cross import data_helper
from src.cross.except_raise import raise_bad_request, raise_not_found
from src.infra.db.db_services import get_db, init_database

from .cases import crud

app = FastAPI()


origins = [
    "http://localhost",
    "https://localhost",
    "http://localhost:8000",
    "http://127.0.0.1:8000" "https://localhost:8000",
    "https://127.0.0.1:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root(request: Request, db: Session = Depends(get_db), shortened_url: Optional[str] = None):
    user_agent = request.headers["user-agent"].split("/")[0]

    if shortened_url:
        if not validators.url(shortened_url):
            raise_bad_request(message=data_helper.BAD_URL_MESSAGE)
    else:
        return data_helper.WELLCOME_MESSAGE
    if target_url := crud.get_target_url_from_db(database=db, shortened_url=shortened_url):
        return dict(target_url=target_url)
    else:
        raise_not_found(request)


@app.post("/create")
def create_url(target_url: str, custom_alias: Optional[str] = None, db: Session = Depends(get_db)):
    if not validators.url(target_url):
        raise_bad_request(message=data_helper.BAD_URL_MESSAGE)
    db_url = crud.create_url(database=db, target_url=target_url, custom_alias=custom_alias)
    return db_url


@app.get("/u/{key}")
def forward_to_target_url(
    request: Request,
    db: Session = Depends(get_db),
):
    user_agent = request.headers["user-agent"].split("/")[0]
    referer = request.headers["referer"].split("/")[-1] if "referer" in request.headers else None
    if user_agent == "Mozilla":
        if referer == "docs":
            return dict(Detail=data_helper.CALL_TARGET_MESSAGE)
        else:
            if target_url := crud.get_target_url_from_db(database=db, shortened_url=request.url._url):
                return RedirectResponse(target_url)
            else:
                raise_not_found(request)
    else:
        return dict(Detail=data_helper.CALL_TARGET_MESSAGE)


@app.on_event("startup")
def on_startup():
    init_database()


@app.get("/healthcheck")
def healtcheck():
    health_msg = {"Health": "It's all right"} if init_database() else {"Health": "Something is wrong!"}
    return health_msg
