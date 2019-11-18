def get_bus(form,request):
    if request.method == 'POST':
        if form.is_valid():
            print('\n\n\n\n')
            avblbus = []
            src = form.cleaned_data['Source']
            dest = form.cleaned_data['Destination']
            for obj in myBuses:
                if src in obj.route and dest in obj.route:
                    avblbus.append(obj.name)
            print("Buses: "+(str(avblbus)))
