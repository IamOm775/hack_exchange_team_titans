from client.models import Cart
from django.shortcuts import render, HttpResponse

# Create your views here.
def ClientDashBoard(request):
    return render(request, 'client/clientdashboard.html')

def cartcheckout(request):
    return render(request, 'client/checkout.html')

def savecart(request):
    if request.method== 'POST':
        x= request.user
        name= request.POST.get('allmyinfluencers')
        listname= request.POST.get('listname')
        campaignname= request.POST.get('campaignname')

        checkout= Cart(name=x, list_name=listname, campaign_name= campaignname, items_json=name)
        checkout.save()
        thank= True
        return render(request, 'client/checkout.html', {'thank': thank} )


