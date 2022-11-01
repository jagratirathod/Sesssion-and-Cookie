from django.core.management.base import BaseCommand
from django.conf import settings
from django.contrib.auth import get_user_model
User = get_user_model()

class Command(BaseCommand):
    help = 'This command will show all the active middleware'

    def handle(self,*args, **kwargs):
        print('Active middleware')
        for i in User.objects.all():
            print(i)
            