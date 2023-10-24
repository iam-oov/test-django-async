from django.http import JsonResponse


from .tasks import waitNSeconds


def slow_response_view(req):
    waitNSeconds.delay(15)
    return JsonResponse({"response": "ok"})


def slow_response_view_2(req):
    return JsonResponse({'ok': 'ok'})
