from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseNotFound
from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    sort = request.GET.get('sort')
    phones = Phone.objects.all()

    if sort == 'max_price':
        phones = phones.order_by("price").reverse()
    elif sort == 'min_price':
        phones = phones.order_by("price")
    elif sort == 'name':
        phones = phones.order_by("name")

    context = {'phones': phones}
    return render(request, template, context=context)


def show_product(request, slug):
    template = 'product.html'

    try:
        phone = Phone.objects.get(slug=slug)
    except ObjectDoesNotExist:
        return HttpResponseNotFound("Phone does not exist")

    context = {'phone': phone}

    return render(request, template, context)