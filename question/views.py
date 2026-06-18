from django.shortcuts import render
from django.http import JsonResponse
from .servise.generator import creat_question
from .models import Pattern
from .servise.calculators.arthmetic import calculate

# Create your views here.
def question_page_view(request, group_type):
    context = {
        "group_type":group_type
    }

    return render(request,'page/questionPage.html',context)

def generate(request,group_type,difficulty):
    patterns = Pattern.objects.filter(group_type=group_type)
    question = creat_question(patterns,difficulty)

    return JsonResponse({
        "status":"correct",
        "value":question["value"]
    })

def check(request,question,answer):
    cor_answer = float(calculate(question))
    status = ""
    if(cor_answer == float(answer)):
        status = "correct"
    else:
        status = "uncorrect"
    return JsonResponse({
        "status":status
    })