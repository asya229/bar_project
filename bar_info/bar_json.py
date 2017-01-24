import json
import os

os.environ['DJANGO_SETTINGS_MODULE'] = 'bar_project.settings'
import django
django.setup()
from django.conf import settings
from barmetro.models import Mainpage,CoordMetro
from django.contrib.auth.models import User
from django.utils import timezone


with open('bar_info1.json', 'r', encoding='cp1251') as f:
    bar = json.load(f)
    for k in bar:
     #   CoordMetro.objects.create(
     #       metroname=k['name'], longitude=k['coords'][1],
     #       latitude=k['coords'][0]
        )


