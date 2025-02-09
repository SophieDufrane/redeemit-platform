from django.shortcuts import render


def handler404(request, exception):
    """Error handler 404 - Page not found"""
    return render(request, 'errors/404.html', status=404)


def handler500(request):
    """Error handler 500 - Internal server error"""
    return render(request, 'errors/500.html', status=500)
