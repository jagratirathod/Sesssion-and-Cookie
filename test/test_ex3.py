import pytest
from django.contrib.auth.models import User

@pytest.mark.django_db
def test_user_create():
    User.objects.create_user('test','test@gmail.com','test')
    User.objects.all().count()
    assert User.objects.count() == 1


@pytest.mark.django_db
def test_user_create1():
    count = User.objects.all().count()
    print(count)    
    assert count == 0
    