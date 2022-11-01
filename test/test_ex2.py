import pytest


@pytest.fixture
def yield_fixture():
    print('Start test phase')
    yield 6
    print('End Test phase')

def test_example(yield_fixture):
    print("--------- run ----------")
    assert yield_fixture == 6
