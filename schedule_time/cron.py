from demoapp.models import Widget
import random 

def print_hello():
    number=random.randint(0,100)
    Widget.objects.create(font_size=number)
    

