from django.shortcuts import render
from event.forms import EventForm
import os


# Create your views here.
def certify(request):
    form = EventForm()
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            event = form.save()
            event.save()
            return render(request, 'event/coupon.html')
        else:
            print(form.errors.as_data())
    return render(request, 'event/form.html', {'form': form})


def coupon(request):
    return render(request, 'event/coupon.html')
