from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import SignupForm, UserUpdateForm, ProfileUpdateForm

from django.core.mail import send_mail
from django.conf import settings

def index(request):
    context = {}
    template = 'index.html'
    return render(request, template, context)


def index2(request):
    context = {}
    template = 'index-2.html'
    return render(request, template, context)


@login_required
def profile(request):
    if request.method == "POST":
        user_form = UserUpdateForm(request.POST, instance = request.user)
        # profile_form = ProfileUpdateForm(request.POST, request.FILES, instance= request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance= request.user.profile)


        if user_form.is_valid and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            # messages.success(request, f'Ypur account has been updated')
            return redirect('profile')
    else:
        user_form = UserUpdateForm(instance = request.user)
        profile_form = ProfileUpdateForm(instance= request.user)

    context = {
        'user_form':user_form,
        'profile_form':profile_form
    }
    template_name = 'profile.html'
    return render(request, template_name, context)



def email(user_email):
    subject = 'Thank you for registering to goodtime'
    message = 'Kindly click the button bellow to authenticate your account'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['ade2adeyinka@gmail.com',user_email,]
    send_mail( subject, message, email_from, recipient_list )
    return redirect('login')

def sendEmail(request):
    send_mail(
    'Subject here',
    'Here is the message.',
    'adetosine6@gmail.com',
    ['ade2adeyinka@gmail.com'],
    fail_silently=False,
    )
    context={}
    template_name = 'mail_confirmation.html'
    return render (request, template_name, context)


def user_login(request):
    context = {}
    template = 'login.html'
    if request.method == "POST":
        username = request.POST['username']
        user_password = request.POST['password']
        user = authenticate(username=username, password=user_password)
        if user:
            login(request, user)
            return redirect('index')
        else:
            context["error"] = "Invalid username or password"
            return render(request, template, context)
    else:
        return render(request, template, context)

def user_logout(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect('index')



def reset_password(request):
    if request.method == "POST":
        email = request.POST['reset_email']
        send_mail(
            'Password Rest',
            'Kindly click on the link <button><button> to reset your mail',
            'adetosine6@gmail.com',
            ['ade2adeyinka@gmail.com', email],
            fail_silently=False,
            )
        

    template_name = 'password/password_reset_form.html'
    return render (request, template_name)

def reset_password_done(request):
    template_name = 'password/password_reset_done.html'
    return render (request, template_name)

def my_account(request):
    template_name = 'my-account.html'
    return render (request, template_name)

def getwishlist(request):
    template_name = 'wishlist.html'
    return render (request, template_name)



def productdetail(request):
    template_name = 'product-details.html'
    return render (request, template_name)


def about_us(request):
    template_name = 'about-us.html'
    return render (request, template_name)

def signup(request):
    context = {}
    template = 'register.html'
    if request.method == "POST":
        username = request.POST['username']
        user_email = request.POST['email']
        user_password1 = request.POST['password1']
        email(user_email)
        user = User.objects.create_user(username=username, email=user_email, password=user_password1)
        return redirect('login')
    else:
        # context['error'] = "Try another user name and make sure your passwords are entered correctly"
        return render(request, template, context)
    return render(request, template)

# def signup(request):
#     context = {}
#     template = 'register.html'
#     if request.method == "POST":
#         form = SignupForm(request.POST)
#         if form.is_valid():
#             print(request.post('email'))
#             email(request.post('email'))
#             form.save()
#             return redirect('login')
#         else:
#             # context['error']= "Invalid input"
#             context = {'error': "Try another user name and make sure your passwords are entered correctly"}
#             return render(request, template, context)
#     else:
#         form = SignupForm()
#     return render(request, template)

