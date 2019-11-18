from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    print(request.path)
    link = str(request.path)
    if link=="/index.html" or link=="/":
        return render(request,'index.html')
    elif link == "/rock_garden.html":
        return render(request,'rock_garden.html')
    elif link == "/sukhna_lake.html":
        return render(request,'sukhna_lake.html')
    elif link == "/rose_garden.html":
        return render(request,'rose_garden.html')
    elif link == "/elante_mall.html":
        return render(request,'elante_mall.html')
    elif link == "/iskcon_temple.html":
        return render(request,'iskcon_temple.html')
    elif link == "/pec.html":
        return render(request,'pec.html')
    elif link == "/buses.html":
        return render(request,'bus_list.html')
    elif link == "/e-ticket.html":
        return render(request,'e-ticket.html')
    elif link == "/ticket.html":
        return render(request,'ticket.html')
