import pytest
from params_test import FILENAME


@pytest.fixture(autouse=True)
def clean_file(filename=FILENAME):
    try:
        with open(filename, 'w'):
            pass
    except Exception() as e:
        print(e)
