from django.core.management.base import BaseCommand
from django.conf import settings

class Command(BaseCommand):
    help = 'This command will show all the active middleware'

    def handle(self,*args, **kwargs):
        print('Active middleware')
        for i in settings.MIDDLEWARE:
            print(i)
            