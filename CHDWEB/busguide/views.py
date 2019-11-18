from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from busguide.forms import FormName
from busguide.busdata import *
from busguide.bus import *
# Create your views here.
def index(request):
    return render(request,'bus_guide.html')

def form_view(request):
    form = FormName()

    if request.method == 'POST':
        form = FormName(request.POST)
        if form.is_valid():
            print('\n\n\n\n')
            avblbus = []
            src = form.cleaned_data['Source']
            dest = form.cleaned_data['Destination']
            for obj in myBuses:
                if src in obj.route and dest in obj.route:
                    avblbus.append(obj.name)
            print("Buses: "+(str(avblbus)))
            buses_list = {"buses":(avblbus),"src":BUS_CH[src],"dest":BUS_CH[dest]}
            return render(request,"bus_list.html",context = buses_list)

    dict = {'form':form}
    return render(request,'bus_guide.html',context = dict)
