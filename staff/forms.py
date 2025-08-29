from django import forms
from .models import Location

class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = ["name", "description", "capacity", "opening_time", "closing_time"]