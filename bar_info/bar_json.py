import json
import os

os.environ['DJANGO_SETTINGS_MODULE'] = 'bar_project.settings'
import django
django.setup()
from django.conf import settings
from barmetro.models import Mainpage,CoordBar
from django.contrib.auth.models import User
from django.utils import timezone


with open('bar_info1.json', 'r', encoding='cp1251') as f:
    bar = json.load(f)
    for k in bar:
        CoordBar.objects.create(
            barname=k['Name'],
            longitude=k['Longitude_WGS84'],
            latitude=k['Latitude_WGS84'],
            address = k['Address'],
            district = k['District'],
            area = k['AdmArea'],
            phone_number = k['PublicPhone'][0]['PublicPhone']
        )


