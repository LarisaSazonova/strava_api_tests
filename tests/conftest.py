import os

import pytest


@pytest.fixture
def get_token():
    return os.environ.get("STRAVA_TEST_TOKEN")
