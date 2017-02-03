from django.core.management.base import BaseCommand, CommandError
from barmetro.models import CoordMetro, CoordBar
from geopy.distance import vincenty
from geopy.geocoders import Nominatim
from geopy.distance import vincenty


def calc_distance(metro, bar):

    metro_point = (metro.latitude, metro.longitude)
    bar_point = (bar.latitude, bar.longitude)
    return (vincenty(metro_point, bar_point).meters)




class Command(BaseCommand):
    help = 'Precalculates bars for distances'

    def add_arguments(self, parser):
        parser.add_argument('some_arg', nargs='+', type=str)


    def handle(self, *args, **options):
        for metro in CoordMetro.objects.all():
            for bar in CoordBar.objects.all():
                distance = calc_distance(metro, bar)
                if distance <= 300:
                    metro.distance_300.add(bar)
                elif distance <= 500:
                    metro.distance_500.add(bar)
                elif distance <= 1000:
                    metro.distance_1000.add(bar)