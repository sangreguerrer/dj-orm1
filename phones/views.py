from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from phones.models import Phone


def index(request):
    template = 'base.html'
    context = request
    return render(request, template)

def show_catalog(request):
    phones = Phone.objects.all()
    sort = request.GET.get('sort')
    if sort == 'name':
        phones = Phone.objects.all().order_by('name')
    elif sort == 'min_price':
        phones = Phone.objects.all().order_by('price')
    elif sort == 'max_price':
        phones = Phone.objects.all().order_by('-price')
    template = 'catalog.html'
    context = {'phones': phones}
    return render(request, template, context)

def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.filter(slug__contains=slug).first()
    context = {'phone': phone}
    return render(request, template, context)