from django.shortcuts import render

def custom_admin_dashboard(request):
    return render(request, 'pages/dashboard.html')

