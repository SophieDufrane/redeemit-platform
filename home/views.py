from django.shortcuts import render

def home(request):
    """
    Renders the home page of the plateform.

    **Template:**
    - home.html: Contains the layout and content for the homepage.

    """
    return render(request, 'home.html')