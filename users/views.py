from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib import messages
from .forms import SignUpForm


# main function, handles signup page
def signup(request):

    # If user is already logged in, send them to home page
    if request.user.is_authenticated:
        return redirect('home')

    # If the form was submitted (POST request)
    # handle submitted form ( username, password, etc.)
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        # Check if the form data is valid (password match, valid email)
        if form.is_valid():
            user = form.save()  # Create the user in the database

            login(request, user)  # Automatically log them in

            # Show success message
            messages.success(request, 'Your account was created successfully.')

            return redirect('home')  # Send them to home page

        else:
            # Show error message if something is wrong
            messages.error(request, 'Please correct the errors below.')

    else:
        # If it's a GET request, just show an empty form
        form = SignUpForm()

    # Render the signup page and pass the form to it
    return render(request, 'registration/signup.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')


def get_user_info(request):
    user = request.user
    context = {
        'first_name': user.first_name,
        'last_name': user.last_name,
        'email_address': user.email_address,
    }
    return render(request, 'account_page.html', context)


def update_user(request):
    if request.method == 'POST':
        user = request.user
        data = request.POST

        user.first_name = data.get('first_name')
        user.last_name = data.get('last_name')
        user.email_address = data.get('email_address')

        user.save()
        messages.success(request, 'Your account was updated successfully.')

    return render(request, 'account_page.html', {})


def delete_user(request):
    if request.method == 'POST':
        user = request.user
        user.delete()
        messages.success(request, 'Your account was deleted successfully.')
        return redirect('home')

    return render(request, 'account_page.html', {})