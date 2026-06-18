from django.shortcuts import render,get_object_or_404
from .models import Guide

# Create your views here.
def guide_page_view(request,group_type):
    guide = get_object_or_404(Guide,group_type=group_type)
    constext = {
        'guide':guide
    }
    return render(request,'page/guidePage.html',constext)