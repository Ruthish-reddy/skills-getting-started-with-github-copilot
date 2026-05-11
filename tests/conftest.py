import copy

import pytest

from src import app

_original_activities = copy.deepcopy(app.activities)

@pytest.fixture(autouse=True)
def reset_activities():
    app.activities.clear()
    app.activities.update(copy.deepcopy(_original_activities))
    yield
