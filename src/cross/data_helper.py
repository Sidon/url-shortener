from src import settings

WELLCOME_MESSAGE = dict(
    detail="Welcome to the URL shortener API :)",
    Help=f"Type: {settings.BASE_URL}/docs on a Mozila agent client",
)

BAD_URL_MESSAGE = "Your provided URL is not valid"
CALL_TARGET_MESSAGE = "Call this endpoint through a Mozila agent."
BAD_PARAMETER_URL = "bad-formated-url"
