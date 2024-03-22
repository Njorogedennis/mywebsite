from django.views.decorators.csrf import csrf_exempt



from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request,'base/home.html')
