import pytest

from data_models import Athlete
from tests.helpers import make_get_request, make_put_request
from dataclasses import asdict


def test_get_athlete(get_token):
    resp = make_get_request("/athlete", get_token)
    assert resp.status_code == 200, "Unexpected status code"
    athlete = extract_athlete_from_resp(resp)
    assert athlete, "Athlete not returned"


def test_change_athlete(get_token):
    resp = make_get_request("/athlete", get_token)
    assert resp.status_code == 200, "Unexpected status code"
    athlete = extract_athlete_from_resp(resp)

    original_weight = athlete.weight
    new_weight = original_weight + 1

    # update the weight
    resp = make_put_request(f"/athlete?weight={new_weight}", get_token, asdict(athlete))
    assert resp.status_code == 200, "Unexpected status code"

    # check that the weight was updated
    resp = make_get_request("/athlete", get_token)
    assert resp.status_code == 200, "Unexpected status code"

    athlete = extract_athlete_from_resp(resp)
    assert athlete.weight == pytest.approx(new_weight), "Weight not updated"

    # return the original weight
    resp = make_put_request(f"/athlete?weight={original_weight}", get_token, asdict(athlete))
    assert resp.status_code == 200, "Unexpected status code"

    # check that the weight was updated
    resp = make_get_request("/athlete", get_token)
    assert resp.status_code == 200, "Unexpected status code"

    athlete = extract_athlete_from_resp(resp)
    assert athlete.weight == pytest.approx(original_weight), "Filed to return original weight"


def extract_athlete_from_resp(resp):
    try:
        athlete = Athlete(**resp.json())
    except TypeError as e:
        raise AssertionError(f"Data does not match data model {e.args}")
    return athlete
