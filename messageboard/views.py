from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from api.models import Ad, PaidAd
from .forms import AdForm
from .filters import AdFilter


def index(request):
    form = Ad.objects.order_by('-date_published')
    filter = AdFilter(request.GET, queryset=form)
    form = filter.qs
    paidad = PaidAd.objects.get()
    context = {'form': form, 'filter': filter, 'paidad': paidad}
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


@login_required
def pin_ad(request, pk):
    ad = get_object_or_404(PaidAd, pk=pk)
    ad.pin()
    return redirect('index')


@login_required
def unpin_ad(request, pk):
    ad = get_object_or_404(PaidAd, pk=pk)
    ad.unpin()
    return redirect('index')
