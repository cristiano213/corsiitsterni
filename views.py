from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# def home(request):
#     return HttpResponse(f"<h1>ciaone sono nasone paolone</h1>")

def home(request):   
    return render(request, "core/homepage.html") 

<<<<<<< HEAD


def annamariafranzoni():
    print("annamariafranzoni")
>>>>>>> esternauno
