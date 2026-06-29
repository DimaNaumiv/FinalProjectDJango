from django.views.decorators.csrf import csrf_exempt
import json
from django.shortcuts import render
from django.http import JsonResponse
from .servise.generator import creat_question
from .models import Pattern
from .servise.calculator import correct_or_no
from .servise.saving import seve_result

from django.shortcuts import render, redirect
from django.urls import reverse

# Create your views here.
def question_page_view(request, group_type):
    context = {
        "group_type":group_type
    }
    min_value = request.GET.get('min') or '0'
    max_value = request.GET.get('max') or '10'

    if request.GET.get('min') != min_value or request.GET.get('max') != max_value:
        base_url = reverse('question', kwargs={'group_type': group_type})
        return redirect(f"{base_url}?min={min_value}&max={max_value}",context)

    return render(request,'page/questionPage.html',context)

@csrf_exempt
def save(request):
    if (request.method == "POST"):

        data = json.loads(request.body)

        group_type = data.get('group_type')
        min_const = data.get('min_const')
        max_const = data.get('max_const')
        qustion = data.get('qustion')
        answer = data.get('answer')
        time =  data.get('time')
        fails =  data.get('fails')

        sessionID = data.get('sessionID')

        result = seve_result(group_type,min_const,max_const,qustion,answer,time,fails,sessionID)

        return JsonResponse({
        "state":result,
    })

@csrf_exempt
def generate(request):
    if (request.method == "POST"):

        data = json.loads(request.body)

        group_type = data.get('group_type')
        min_value = int(data.get('min') or 0)
        max_value = int(data.get('max') or 10)

        patterns = Pattern.objects.filter(group_type=group_type)
        question = creat_question(patterns,min_value,max_value)

        return JsonResponse({
        "status":"correct",
        "value":question["value"]
    })

@csrf_exempt
def check(request):
    if (request.method == "POST"):

        data = json.loads(request.body)

        group_type = data.get('group_type')
        question = data.get('question')
        answer = data.get('answer')

        status = correct_or_no(answer,group_type,question)
    return JsonResponse({
        "status":status
    })