from django.shortcuts import render, redirect
from .forms import RegisterForm

# from django.contrib.auth.models import User  # replaced by CustomUser
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.conf import settings
from django.core.mail import EmailMessage
from django.utils import timezone
from django.urls import reverse
from .models import *  # includes CustomUser

@login_required
def Home(request):
    return render(request,'shop/home.html')

def RegisterView(request):
    if request.method == "POST":
        # get posted fields:
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # field validation:
        user_data_has_error = False
        if CustomUser.objects.filter(username=username).exists():
            user_data_has_error = True
            messages.error(request, "Username already exists")
        if CustomUser.objects.filter(email=email).exists():
            user_data_has_error = True
            messages.error(request, "Email already exists")
        if len(password) < 5:
            user_data_has_error = True
            messages.error(request, "Password must be at least 5 characters")
        if user_data_has_error:
            return redirect('users:register')
        else:
            # create new user in database:
            new_user = CustomUser.objects.create_user(
                first_name=first_name,
                last_name=last_name,
                email=email,
                username=username,
                password=password
            )
            messages.success(request, "Account created. Login now")
            return redirect('users:login')
    else:
        return render(request,'registration/register.html')

def LoginView(request):
    """NB: Do not call this view "login", to prevent clashes with imported login() method"""
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            return redirect('users:home')

        else:
            messages.error(request, "Invalid login credentials")
            return redirect('users:login')

    else:
        return render(request,'registration/login.html')

def LogoutView(request):
    logout(request)
    return redirect("users:login")

def ForgotPassword(request):
    if request.method == "POST":
        email = request.POST.get('email')

        try:
            user = CustomUser.objects.get(email=email)

            new_password_reset = PasswordReset(user=user)
            new_password_reset.save()

            password_reset_url = reverse('users:reset-password', kwargs={'reset_id': new_password_reset.reset_id})

            #                            http/https         127.0.0.1:8000      /reset-password/<reset_id>
            full_password_reset_url = f'{request.scheme}://{request.get_host()}{password_reset_url}'

            email_body = f'Reset your password using the link below:\n\n\n{full_password_reset_url}'

            email_message = EmailMessage(
                'Reset your password', # email subject
                email_body,
                settings.EMAIL_HOST_USER, # email sender
                [email] # email  receiver
            )

            email_message.fail_silently = True
            email_message.send()

            return redirect('users:password-reset-sent', reset_id=new_password_reset.reset_id)

        except CustomUser.DoesNotExist:
            messages.error(request, f"No user with email '{email}' found")
            return redirect('users:forgot-password')

    return render(request, 'registration/forgot_password.html')

def PasswordResetSent(request, reset_id):

    if PasswordReset.objects.filter(reset_id=reset_id).exists():
        return render(request, 'registration/password_reset_sent.html')
    else:
        # redirect to forgot password page if code does not exist
        messages.error(request, 'Invalid reset id')
        return redirect('users:forgot-password')

def ResetPassword(request, reset_id):

    try:
        password_reset_id = PasswordReset.objects.get(reset_id=reset_id)

        if request.method == "POST":
            # Get values from POST data
            password = request.POST.get('password')
            confirm_password = request.POST.get('confirm_password')

            # Verify that both passwords are valid and match
            passwords_have_error = False
            if password != confirm_password:
                passwords_have_error = True
                messages.error(request, 'Passwords do not match')
            if len(password) < 5:
                passwords_have_error = True
                messages.error(request, 'Password must be at least 5 characters long')

            # Verify that the reset link hasn't expired
            expiration_time = password_reset_id.created_when + timezone.timedelta(minutes=10)
            if timezone.now() > expiration_time:
                passwords_have_error = True
                messages.error(request, 'Reset link has expired')
                password_reset_id.delete()

            if not passwords_have_error:
                # Set password for user and delete password reset object
                user = password_reset_id.user
                user.set_password(password)
                user.save()
                password_reset_id.delete()

                messages.success(request, 'Password reset. Proceed to login')
                return redirect('users:login')
            else:
                # redirect back to password reset page and display errors
                return redirect('users:reset-password', reset_id=reset_id)


    except PasswordReset.DoesNotExist:

        # redirect to forgot password page if code does not exist
        messages.error(request, 'Invalid reset id')
        return redirect('users:forgot-password')

    return render(request, 'registration/reset_password.html')