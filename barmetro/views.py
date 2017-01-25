from django.shortcuts import render, get_object_or_404
from .models import CoordMetro

def page_list(request):
    coords = CoordMetro.objects.all()[:20]
    return render(request, 'barmetro/page_list.html', {'coords': coords})

def page_metro(request, pk):
    station = get_object_or_404(CoordMetro, pk=pk)
    return render(request, 'barmetro/page_metro.html', {'station': station})