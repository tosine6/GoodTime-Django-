from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from . import views


urlpatterns = [
    path('',views.index, name='index'),
    path('index-2',views.index2, name='index-2'),
    path('signup/',views.signup, name='signup'),
    path('login/',views.user_login, name='login'),
    # path('logout/',views.user_logout, name='logout'),
    path('profile/',views.profile, name='profile'),
    path('myaccount/',views.my_account, name='my-account'),
    path('myaccount/logout/',views.user_logout, name='my-account'),
    # path('login-register/',views.user_login, name='login-register'),
    path('auth/', include('django.contrib.auth.urls')),
    path('about-us/',views.about_us, name='about-us'),
    path('wishlist/',views.getwishlist, name='wishlist'),
    path('product-details/',views.productdetail, name='product-details'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)