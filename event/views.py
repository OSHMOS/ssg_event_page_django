from django.shortcuts import render

# Create your views here.


def upload(request):
    if request.method == 'POST':
        pass
    return render(request, 'event/form.html')
