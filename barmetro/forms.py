from django import forms
from .models import CoordMetro,CoordBar


class BarSearchFrom(forms.Form):
    metro_station = forms.ModelChoiceField(widget=forms.Select(), label='Выбери станцию Метро', queryset=CoordMetro.objects.all())


def __init__(self, *args, **kwargs):
    super(BarSearchFrom, self).__init__(*args, **kwargs)

    metro_station = [
        ('', ('select office')),
        ('office 1', 'office 1'),
        ('office 2', 'office 2'),
    ]
    self.fields['office'].choices = metro_station

