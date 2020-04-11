from django.shortcuts import render
from django.http import HttpResponse
import json
xx_list = [
    {'tx': '', 'xx': ''},
    {'tx': '', 'xx': ''},
    {'tx': '', 'xx': ''},
    {'tx': '', 'xx': ''},
    {'tx': '', 'xx': ''},
    {'tx': '', 'xx': ''},
    {'tx': '', 'xx': ''},
    {'tx': '', 'xx': ''},
    {'tx': '', 'xx': ''},
    {'tx': '', 'xx': ''},
]
# Create your views here.


def wan(request):
    return render(request, 'game/lt.html')


def gat_xx(request):
    while len(xx_list) > 10:
        del xx_list[0]
    res = json.dumps(xx_list)
    return HttpResponse(res, content_type='application/json')


def fs_xx(request):
    u_name = request.session.get('u_name')
    xx = request.GET.get('xx')
    xx_list.append({'tx': u_name, 'xx': xx})
    return HttpResponse('ok')
