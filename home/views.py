from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import CustomSignupForm

def home(request):
    """
    Renders the home page of the plateform.

    **Template:**
    - home.html: Contains the layout and content for the homepage.

    """
    return render(request, 'home.html')


def signup_view(request):
    """
    Handles user's registration with custom form.

    - Displays the signup form when accessed via GET.
    - Processes form submission when accessed via POST.
    - Creates a new user, hashes their password, and logs them in.
    """
    if request == "POST":
        # Populate form with user input
        form = CustomSignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            # Don't save yet (we need to hash the password)
            user.set_password(form.cleaned_data["password"])
            user.save()
            login(request, user)
            return redirect("home")
    
    else:
        # If GET request, show an empty form
        form = CustomSignupForm()
    
    return render(request, "account/signup.html", {"form": form})
