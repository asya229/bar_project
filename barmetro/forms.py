from django import forms
from .models import CoordMetro,CoordBar


class BarSearchFrom(forms.Form):
    metro_station = forms.ModelChoiceField(label='Метро', queryset=CoordMetro.objects.all())








