from django.shortcuts import render

from django.http import JsonResponse
from .tasks import waitNSeconds


def slowResponseView(req):
    waitNSeconds.delay(15)
    return JsonResponse({"response": "ok"})


def slowResponseView2(req):
    return JsonResponse({'ok': 'ok'})
