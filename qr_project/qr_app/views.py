from django.shortcuts import render
from django.http import HttpResponse

mylist = [
    {
    "author":"Mustafa",
    "title": "Baslik",
    "content":"Hi guys welcome and bye",
    },
    {
    "author":"Mehmet",
    "title": "Baslik2",
    "content":"Veni vici vokke",
    }
    
    ]
def index(request):
    context = {
        "mylist":mylist
    }
    return render(request,"qr_app/home.html",context)
    #return HttpResponse("Hello, world. You're at the polls index.")
    
def bathroom(request):
    return render(request,"qr_app/bathroom.html",{"title":"dirty"})