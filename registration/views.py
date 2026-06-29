import json
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from registration.servise import servise

# Create your views here.

def ragistration_page_view(request):
    return render(request,'page/ragistrationPage.html')

@csrf_exempt
def ragistrate_request(request):
    result = None
    if (request.method == "POST"):

        data = json.loads(request.body)

        first_name = data.get('first_name')
        last_name = data.get('last_name')
        password = data.get('password')

        result = servise.registrate(first_name,last_name,password)

    return JsonResponse({
        "state" : result["state"],
        "session_code" : result["session_code"]
    })

@csrf_exempt
def check_request(request):
    result = None
    if (request.method == "POST"):

        data = json.loads(request.body)

        first_name = data.get('first_name')
        last_name = data.get('last_name')
        password = data.get('password')

        result = servise.check(first_name,last_name,password)

    return JsonResponse({
        "state" : result["state"],
        "session_code" : result.get("session_code", None)
    })

def delete(request, session_code):
    state = servise.delete_session(session_code)
    return JsonResponse({
        "state" : state
    })

def check_session(request,session_code,):
    state = servise.check_session_code(session_code)
    return JsonResponse({
        "state" : state
    })
    return True
