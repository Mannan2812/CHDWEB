from django.shortcuts import render
from eticket.forms import TicketForm
import qrcode
import random
import math
import datetime


# Create your views here.

# Create your views here.



def form_view(request):
    form =  TicketForm()

    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            dest = {'rg':'Rock Garden','rsg':'Rose Garden','sl':'Sukhna Lake','it':'Iskcon Temple'}
            a = form.cleaned_data['destination']
            v = form.cleaned_data['visitors']
            d = datetime.date.today().strftime("%B %d, %Y")

            val = math.ceil(random.random()*1000000000000000+1)
            qr = qrcode.make(val)
            qr.save('myqr.jpg')
            dict = {'dest':dest[a],'visitors':v,'date':d,'val':val,'qr':qr}
            return render(request,'ticket.html',context = dict)

    dict = {'form':form}



    return render(request,'e-ticket.html',context = dict)
