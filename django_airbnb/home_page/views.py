from django.shortcuts import render

# Create your views here.

def home_view(request):

    #import pudb; pu.db()
    return render(request, "home_page/home_page.html")
