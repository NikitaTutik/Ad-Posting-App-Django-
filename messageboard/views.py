from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from api.models import Ad
from .forms import AdForm
from . filters import AdFilter


def index(request):
    form = Ad.objects.order_by('-date_published')
    filter = AdFilter(request.GET, queryset=form)
    form = filter.qs
    context = {'form': form, 'filter': filter}
    return render(request, 'messageboard/mainpage.html', context)


@login_required
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
            form = form.save(commit=False)
            form.author = request.user
            form.save()
            return redirect('index')


@login_required
def delete_ad(request, id):
    ad = Ad.objects.get(pk=id)
    ad.delete()
    return redirect('index')

