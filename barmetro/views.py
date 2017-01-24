from django.shortcuts import render
from .models import CoordMetro

def page_list(request):
    coords = CoordMetro.objects.all()[:20]
    return render(request, 'barmetro/page_list.html', {'coords': coords})

