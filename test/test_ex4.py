import pytest
from django.contrib.auth.models import User
from conftest import *

# @pytest.fixture()
# def user_1(db):
#     user= User.objects.create_user("test-user")
#     print("create user -",user)
#     return user

# def test_set_check_password1(user_1):
#     print("check password1")
#     assert user_1.username == "test-user"

# def test_set_check_password2(user_1):
#     print("check password2")
#     assert user_1.username == "test-user"


# # @pytest.mark.django_db
# def test_set_check_password(user_1):
#     user_1.set_password("new password")
#     assert user_1.check_password("new-password") is True

# # @pytest.fixture()
# def user_1(db):
#     user = User.objects.create_user("test-user")

@pytest.fixture()
def test_new_user(new_user2):
    print("jkjk")
    print(new_user2.is_staff)
    assert new_user2.is_staff
