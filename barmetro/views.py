from django.shortcuts import render, get_object_or_404
from .models import CoordMetro,CoordBar

def page_list(request):
    coords = CoordMetro.objects.all()[:30]
    coords_for_bar = CoordBar.objects.all()[:20]
    return render(request, 'barmetro/page_list.html', {'coords': coords, 'coords_for_bar': coords_for_bar})

def page_metro(request, pk):
    station = get_object_or_404(CoordMetro, pk=pk)
    return render(request, 'barmetro/page_metro.html', {'station': station})

def page_bar(request, pk):
    bar = get_object_or_404(CoordBar, pk=pk)
    return render(request, 'barmetro/page_bar.html', {'bar': bar})


