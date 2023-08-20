from django.shortcuts import render

# Create your views here.
from django.contrib.auth.decorators import login_required

@login_required(login_url='users:login')
def dashboardPage(request):

    context = {

    }
    return render(request, 'content/dashboard.html', context)