import requests

STRAVA_BASE_URL = "https://www.strava.com/api/v3"


def make_get_request(url, token,  params=None):
    kwargs = {}
    url = f"{STRAVA_BASE_URL}/{url}"
    headers = {"Authorization": f"Bearer {token}"}

    if params is not None:
        kwargs = {"params": params}

    return requests.get(url, headers=headers, **kwargs)


def make_put_request(url, token, body=None, params=None):
    kwargs = {}
    url = f"{STRAVA_BASE_URL}/{url}"
    headers = {"Authorization": f"Bearer {token}"}

    if body is not None:
        kwargs = {"json": body}

    if params is not None:
        kwargs = {"params": params}

    return requests.put(url, headers=headers, **kwargs)
