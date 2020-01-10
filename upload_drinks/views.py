from django.shortcuts import render



def upload_drink(request):
    return render (request, 'upload_drinks.html')


def drinks(request):
    return render (request, 'drinks.html')