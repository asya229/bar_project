from django import forms
from .models import CoordMetro,CoordBar


class BarSearchFrom(forms.Form):
    metro_station = forms.ModelChoiceField(widget=forms.Select(attrs={'color': 'yellow'}), label='Выбери станцию Метро', queryset=CoordMetro.objects.all())





