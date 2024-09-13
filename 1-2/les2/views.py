from django.http import HttpResponse
import datetime
from django.shortcuts import render
from django.core.paginator import Paginator

def hello(request):
    context = {
        'test': 5,
        'data': [1, 5, 8, 10],
        'val': "hello",
    }
    return render(request, 'les1.html', context)

def sum(request, op1, op2):
    result = op1 + op2
    return HttpResponse(f'Sum = {result}')

CONTENT = [str(i) for i in range(10000)]

def pagi(request):
    page_number = int(request.GET.get("page", 1))
    paginator = Paginator(CONTENT, 10)
    page = paginator.get_page(page_number)
    context = {
        'page': page
    }
    return render(request, 'pagi.html', context)

# def time(request):
#     return HttpResponse(f"Time = {datetime.datetime.now().strftime('%H:%M:%S')}")
