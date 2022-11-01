import pytest

# Create your tests here.

@pytest.fixture(scope="session")
def fixture_1():
    print('---------- hello ------')
    return 1

def test_example1(fixture_1):
    print('---------- hii ------')
    num =  fixture_1
    print(num)
    assert num == 1

def test_example2(fixture_1):
    print('---------- hiiiiiiii ------')
    num =  fixture_1
    assert num == 1






# @pytest.marks.skip
# @pytest.marks.xfail

# @pytest.marks.slow
# def test_example():
#     assert 1 == 1

# def test_example1():
#     assert 1 == 1




    

    


