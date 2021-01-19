from django.shortcuts import render,redirect
from api.models import Ad
from .forms import AdForm


def index(request):
    form = Ad.objects.all()
    context = {'form': form}
    return render(request, 'messageboard/mainpage.html', context)


def add_ad(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = AdForm()
        else:
            ad = Ad.objects.get(pk=id)
            form = AdForm(instance=ad)
        return render(request, 'messageboard/add_ad.html', {'form': form})
    elif request.method == "POST":
        if id == 0:
            form = AdForm(request.POST)
        else:
            ad = Ad.objects.get(pk=id)
            form = AdForm(request.POST, instance=ad)
        if form.is_valid():
            form.save()
            return redirect('index')


def delete_ad(request):
    return


