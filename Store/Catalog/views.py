from django.shortcuts import render


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
    return render(request, '../Templates/store/graphiccard.html')
