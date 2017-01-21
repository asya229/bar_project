import os


os.environ['DJANGO_SETTINGS_MODULE'] = 'bar_project.settings'
import django
django.setup()
from django.conf import settings
from barmetro.models import Mainpage
from django.contrib.auth.models import User
from django.utils import timezone

Mainpage.objects.create( title='Metro', text='Bar', published_date=timezone.now())

Mainpage.objects.all()