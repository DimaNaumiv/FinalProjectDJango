from django.shortcuts import render

# Create your views here.

def ragistration_page_view(request):
    return render(request,'page/regiragistrationPage.html')

def save_user(request, name,password):
    return True
