from django import forms

class TicketForm(forms.Form):
    choice = [("rg","Rock Garden"),("sl","Sukhna Lake"),("rsg","Rose Garden"),("it","Iskcon Temple")]
    destination = forms.CharField(widget = forms.Select(choices = choice,attrs={'class':'form-control','id':'dest'}))
    visitors = forms.CharField( widget=forms.TextInput(attrs={'type':'number','class':'form-control','value':1,'min':1,'max':10,'id':'visits'}))
