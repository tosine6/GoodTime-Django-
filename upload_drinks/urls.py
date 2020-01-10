from django.urls import path
from . import views


urlpatterns = [
    path('',views.upload_drink,name ='upload-drink'),
    path('drinks',views.drinks,name ='drinks'),
]