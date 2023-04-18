from django.shortcuts import render
from event.forms import EventForm
# Create your views here.


def upload(request):
    form = EventForm()
    if request.method == 'POST':
        pass
    return render(request, 'event/form.html', {'form': form})
