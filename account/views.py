from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm



# Create your views here.
def indexView(request):
    return render(request,'index.html')

def dashboardView(request):
    return render(request,'dashboard.html')

def registerView(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'home.html')
    else:
        form = UserCreationForm()   
        
    return render(request,'register.html',{'form':form})


