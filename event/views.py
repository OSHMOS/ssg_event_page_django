from django.shortcuts import render
from event.forms import EventForm
# Create your views here.


def certify(request):
    form = EventForm()
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            event = form.save()
            event.save()
            return render(request, 'event/thx.html')
        else:
            print(form.errors.as_data())
    return render(request, 'event/form.html', {'form': form})
