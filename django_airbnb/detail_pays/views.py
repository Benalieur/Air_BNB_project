from django.shortcuts import render

# Create your views here.

def detail_pays_view(request):
    return render(request, 'detail_pays/detail_pays.html')
