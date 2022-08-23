from django.shortcuts import render


def sidebar(request):
    return render(request, 'frontend/sidebar.html')


def static_db(request):
    return render(request, 'frontend/static_db.html')