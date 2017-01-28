import os


os.environ['DJANGO_SETTINGS_MODULE'] = 'bar_project.settings'
import django
django.setup()
from django.conf import settings
from barmetro.models import Mainpage,CoordMetro
from django.contrib.auth.models import User
from django.utils import timezone

print(CoordMetro.objects.filter(latitude__contains="55"))