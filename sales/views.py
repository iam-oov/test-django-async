from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
import redis
from django.conf import settings
import json
from django.shortcuts import render

from django.http import JsonResponse
from .tasks import waitNSeconds


def slow_response_view(req):
    waitNSeconds.delay(15)
    return JsonResponse({"response": "ok"})


def slow_response_view_2(req):
    return JsonResponse({'ok': 'ok'})


# Connect to our Redis instance
redis_instance = redis.StrictRedis(
    host=settings.REDIS_HOST,
    port=settings.REDIS_PORT,
    db=settings.REDIS_DB
)


@api_view(['GET'])
def test_redis(request, *args, **kwargs):
    items = {}
    count = 0
    for key in redis_instance.keys("*"):
        items[key.decode("utf-8")] = redis_instance.get(key)
        count += 1
    response = {
        'count': count,
        'msg': f"Found {count} items.",
        'items': items
    }
    return Response(response, status=200)
