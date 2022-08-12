from django.shortcuts import redirect
from django.http import HttpResponse
from django.contrib.auth import logout
from .forms import User
import random
def password(request):
    if request.user.is_authenticated:
        logout(request)
        return HttpResponse(random.sample(range(10),4))
    else:
        return redirect("/login")