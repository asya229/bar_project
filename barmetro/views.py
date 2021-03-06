from django.shortcuts import render, get_object_or_404
from .models import CoordMetro,CoordBar
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from .forms import BarSearchFrom
from django.http import JsonResponse


def page_list(request):
    coords = CoordMetro.objects.all()
    coords_for_bar = CoordBar.objects.all()
    form_choice_metro = BarSearchFrom()
    context = {'metro_station': coords, 'coords_for_bar': coords_for_bar,'form_choice_metro':form_choice_metro}
    return render(request, 'barmetro/page_list.html', context)

def page_metro(request, pk):
    station = get_object_or_404(CoordMetro, pk=pk)
    return render(request, 'barmetro/page_metro.html', {'station': station})

def page_bar(request, pk):
    bar = get_object_or_404(CoordBar, pk=pk)
    return render(request, 'barmetro/page_bar.html', {'bar': bar})


def bar_view(request):
   if request.method == 'POST':
       #print ('пост',request.POST)

       form = BarSearchFrom(request.POST)

       bars_300 =[]
       bars_500 =[]
       bars_1000 =[]
       selected_station = []
       metro_id = []

       if form.is_valid():
           print(form.cleaned_data['metro_station'])
           selected_station = form.cleaned_data['metro_station']
           print('пост', request.POST)
           bars_300 = selected_station.distance_300.all()
           #print(bars_300)
           bars_500 = selected_station.distance_500.all()
           bars_1000 = selected_station.distance_1000.all()


   else:
       print('not valid')
       bars_300 = []
       bars_500 = []
       bars_1000 = []
       selected_station = []
       metro_id = []
       #form = BarSearchFrom()
   return render(request,
       'barmetro/bars.html',
       {

           'bars_300': bars_300,
           'bars_500': bars_500,
           'bars_1000': bars_1000,
           'selected_station': selected_station,
           'metro_id': metro_id,
       }
   )

def geodata_metro(request, pk):
    station = get_object_or_404(CoordMetro, pk=pk)
    s300 = station.distance_300.all()
    s500 = station.distance_500.all()
    s1000 = station.distance_1000.all()
    features = []
    data = {}
    for bar in s300:
        features.append({"type": "Feature", "geometry": {"type": "Point", "coordinates": [float(bar.longitude), float(bar.latitude)]},"properties": {}})
        data = {"type": "FeatureCollection", "features": features}
    #return JsonResponse(data, safe=False)

    for bar in s500:
        features.append({"type": "Feature", "geometry": {"type": "Point", "coordinates": [float(bar.longitude), float(bar.latitude)]},"properties": {}})
        data = {"type": "FeatureCollection", "features": features}
    #return JsonResponse(data, safe=False)

    for bar in s1000:
        features.append({"type": "Feature", "geometry": {"type": "Point", "coordinates": [float(bar.longitude), float(bar.latitude)]},"properties": {}})
        data = {"type": "FeatureCollection", "features": features}
    return JsonResponse(data, safe=False)







