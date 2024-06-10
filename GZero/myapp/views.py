from django.shortcuts import render

# Create your views here.
  
def home(request): 
    return render(request, "home.html") 
  
def projects(request): 
    return render(request, "projects.html") 
  
def contact(request): 
    return render(request, "contact.html")
def index(request):
    return render(request, "arte.html")
def menu(request):
    return render(request, "menu.html")