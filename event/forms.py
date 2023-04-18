from django import forms
from .models import Event


# Create your models here.
class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = '__all__'
