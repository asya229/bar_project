from django.shortcuts import render, get_object_or_404
from .models import CoordMetro,CoordBar
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from .forms import BarSearchFrom



def page_list(request):
    coords = CoordMetro.objects.all()
    coords_for_bar = CoordBar.objects.all()
    # form_choice_metro = BarSearchFrom()
    context = {'metro_station': coords, 'coords_for_bar': coords_for_bar,}
    return render(request, 'barmetro/page_list.html', context)

def page_metro(request, pk):
    station = get_object_or_404(CoordMetro, pk=pk)
    return render(request, 'barmetro/page_metro.html', {'station': station})

def page_bar(request, pk):
    bar = get_object_or_404(CoordBar, pk=pk)
    return render(request, 'barmetro/page_bar.html', {'bar': bar})


def bar_view(request):
   if request.method == 'POST':
       print (request.POST)
       form = BarSearchFrom(request.POST)

       bars_300 =[]
       bars_500 =[]
       bars_1000 =[]
       if form.is_valid():
           print(form.cleaned_data['metro_station'])
           selected_station = form.cleaned_data['metro_station']
           bars_300 = selected_station.distance_300.all()
           print(bars_300)
           bars_500 = selected_station.distance_500.all()
           bars_1000 = selected_station.distance_1000.all()
   else:
       bars_300 = []
       bars_500 = []
       bars_1000 = []
       #form = BarSearchFrom()
   return render(request,
       'barmetro/bars.html',
       {

           'bars_300': bars_300,
           'bars_500': bars_500,
           'bars_1000': bars_1000,
       }
   )









