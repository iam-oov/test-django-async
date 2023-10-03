from django.shortcuts import render

from django.http import JsonResponse
from .tasks import waitNSeconds


def slowResponseView(request):
    waitNSeconds.delay(15)
    return JsonResponse({"response": "ok"})
