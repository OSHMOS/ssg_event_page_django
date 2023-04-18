from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from event.forms import EventForm
from django.conf import settings
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


def download(request):
    try:
        with open(os.path.join(settings.BASE_DIR, 'static', 'img', 'coupon.jpg'), 'rb') as f:
            return HttpResponse(f.read(), content_type='image/jpg')
    except IOError:
        return HttpResponseNotFound('<h1>Page not found</h1>')
