from atexit import register
from django.shortcuts import redirect, render
from django.views import View
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth import login 
from django.contrib import messages

# Create your views here.
class RegisterView(View):
    def get(self, request):
        form = UserCreationForm()
        return render(request,"register/register.html",{"form":form})

    def post(self, request):
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('Home')
        else:
            for msg in form.error_messages:
                messages.error(request, form.error_messages[msg])
            return render(request,"register/register.html",{"form":form})
            

