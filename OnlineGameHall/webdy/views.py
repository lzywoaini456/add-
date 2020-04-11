from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from .models import Video, VideoType, VideoComment, Likes
from user.models import User, WatchHistory
from OnlineGameHall.settings import BASE_DIR
from django.db.models import *
import random
from .task import task_test
# Create your views here.


def index_view(request):
    if request.method == 'GET':
        return render(request, 'webdy/index.html')

def favicon_ico(requsest):
    return HttpResponseRedirect('/static/imgs/info.png')


def add_view(request):
    if request.method == "GET":
        return render(request, 'webdy/add.html')
    elif request.method == "POST":
        js = request.POST.get('js')
        if not js:
            return JsonResponse({'code': '10101', 'error': 'No js'})
        myfile = request.FILES['my_file']
        if not myfile:
            return JsonResponse({'code': '10102', 'error': 'No myfile'})
        lx = request.POST.get('lx')
        if not lx:
            return JsonResponse({'code': '10103', 'error': 'No lx'})

        name = request.session.get('u_name')
        dx = User.objects.get(u_name=name)
        sy = len(dx.video_set.all()) + 1
        lj = '/static/video/' + lx + '/' + name + '_' + str(sy) + '.mp4'
        ty = VideoType.objects.get(type_name=lx)
        Video.objects.create(video_name=js, video_likes=0, video_comment=0, video_files=lj, video_type=ty, video_user=dx)
        file_path = BASE_DIR + lj
        task_test.delay(file_path, myfile)

        return JsonResponse({'code': '200', 'data': 'upload is OK'})


def get_sp_view(request):
    u_id = request.session.get('u_id')
    print(u_id)
    try:
        u_dx = User.objects.get(id=u_id)
    except:
        return JsonResponse({'error': '小伙子去登陆'})
    co = Likes.objects.values('l_type').filter(l_user=u_id)
    do = co.annotate(Count=Count('l_type')).order_by('-Count')
    # 如何他最喜欢的类型有值
    # 类型对象
    # while True:
    while True:
        if random.randint(0, 4) and do:
            lx_id = do[0]['l_type']
            v_type = VideoType.objects.get(id=lx_id)
        else:
            v_type = random.choice(VideoType.objects.all())
            if not v_type:
                continue
        # 看过的
        ls = [i.w_v_id for i in WatchHistory.objects.filter(w_u_id=u_id)]
        # 因为该类型可能没有视频所以要try一下
        try:
            sp = random.choice(v_type.video_set.exclude(id__in=ls))
        except:
            continue
        data = {'v_id': sp.id, 'v_jj': sp.video_name, 'video': sp.video_files, 'u_tx': str(u_dx.u_tx), 'u_name': u_dx.u_name, 'dzs': sp.video_likes, 'pls': sp.video_comment}
        return JsonResponse({'code': 200, 'data': data})


def get_pl_view(request):
    video = request.GET.get('video')
    sp = VideoComment.objects.filter(com_video=video)
    fpl = []
    home = {}
    for i in sp:
        dx = User.objects.get(id=i.com_user)
        if i.com_ba == 0:
            c = {'id': i.id, 'username': dx.u_name, 'user_tx': str(dx.u_tx), 'pl': i.com_text}
            fpl.append(c)
        else:
            home.setdefault(i.com_ba, []).append({'id': i.id, 'username': dx.u_name, 'user_tx': str(dx.u_tx), 'pl': i.com_text})
    for i in fpl:
        i['zpl'] = home.get(i['id'], [])
    return JsonResponse({'code': 200, 'date': fpl})


def write_pl_view(request):
    video_id = request.GET.get('video')
    user_id = request.GET.get('u_id')
    f_id = request.GET.get('f_id')
    if not f_id:
        f_id = 0
    f_id = int(f_id)
    text = request.GET.get('pl')
    if not text or len(text) >= 30:
        return JsonResponse({'error': '文字太多'})
    VideoComment.objects.create(com_video=video_id, com_ba=f_id, com_user=user_id, com_text=text)
    return JsonResponse({'code': 200})


def get_dz_view(request):
    user = request.session.get('u_name')
    video = request.GET.get('video')
    pass

