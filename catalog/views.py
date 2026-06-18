from django.shortcuts import render
from .models import Major
# Create your views here.
def catalog_page_view(request):
    categories = Major.objects.all()

    context = {
        'categories' : categories,
    }

    return render(request,"page/catalogPage.html",context)