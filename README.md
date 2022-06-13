# Url Shortener

A simple FastAPI project that uses SQLAlchemy, SQLModel, SQlite, Alembic, and Docker.
This project had developed to attend the Bemobi challenge [see description here.](readme-bemobi.md)

## How to use this project:

### Docker
```sh
$ docker-compose up -d --build
$ docker-compose exec web alembic upgrade head
```

### Sanity check:
[http://localhost:8004/healthchek](http://localhost:8004/healthchek)

### API Documentation:
[http://localhost:8004/docs](http://localhost:8004/docs)

### Generation Aliases:
To generate the aliases, I chose the secrets package that is already built into python, a short summary about it:  
"The secrets module is used for generating cryptographically strong random numbers suitable for
managing data such as passwords, account authentication, security tokens, and related secrets."  
[From python documentation](https://docs.python.org/3/library/secrets.html)

### To test the forward functionality:
- Create a shortened URL ([see this topic of docs](http://localhost:8004/docs#/default/create_url_create_post));
- Copy (Control-c) the URL field in the body response;
- Paste the URL in a browser like chrome.