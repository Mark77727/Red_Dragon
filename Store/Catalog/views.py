from django.shortcuts import render


""" import forms for filter """

from .filters import CatalogFilter


""" import modules """


from django.core.paginator import Paginator


""" import models """


from .models import Catalog


"""View"""


def index(request):
    return render(request, '../Templates/page/index.html')


def base(request):
    return render(request, '../Templates/page/base.html')


def catalog(request):
    return render(request, '../Templates/catalog/catalog.html')


def cpu(request):
    return render(request, '../Templates/store/cpu.html')


def graphiccard(request):
    graphiccard_catalog = Catalog.objects.all()
    catalog_filter = CatalogFilter(request.GET, queryset=graphiccard_catalog)
    graphiccard_catalog = catalog_filter.qs
    graphiccard_catalog_price = Catalog.objects.filter(price__gte=0, price__lte=1000000)

    return render(request, '../Templates/store/graphiccard.html', {'graphiccard_catalog': graphiccard_catalog,
                                                                   'catalog_filter': catalog_filter,
                                                                   'graphiccard_catalog_price': graphiccard_catalog_price})