import json,hashlib,re, datetime, time
from .. import models
from django.views.decorators.csrf import csrf_exempt, ensure_csrf_cookie
from django.http import HttpResponse, JsonResponse

@ensure_csrf_cookie
def user_storezip(request):
    file = request.FILES['zip']
    md5 = hashlib.md5()
    md5.update(str(int(time.time())).encode('utf8'))
    name = md5.hexdigest() + '.' + file.name.split('.')[1]
    print("name: " + name)
    with open('./static/upload/package/' + name, 'wb') as destination:
        for chunk in file.chunks():
            destination.write(chunk)
    return JsonResponse({'url': '/static/upload/package/' + name})

@ensure_csrf_cookie
def user_storepic(request):
    file = request.FILES['pic']
    md5 = hashlib.md5()
    md5.update(str(int(time.time())).encode('utf8'))
    name = md5.hexdigest() + '.' + file.name.split('.')[1]
    print("name: " + name)
    with open('./static/upload/img/' + name, 'wb') as destination:
        for chunk in file.chunks():
            destination.write(chunk)
    return JsonResponse({'url': '/static/upload/img/' + name})