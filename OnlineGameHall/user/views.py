"""
    视图函数
"""
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core import mail
from .models import User
import random
# Create your views here.


def index_view(request):
    """
    主业视图函数
    :param request: 请求
    :return: 主页内容
    """
    if request.method == "GET":
        pass


def login_view(request):
    """
    登陆视图
    :param request:
    :return:
    """
    if request.method == "GET":
        return render(request, 'user/login.html')
    elif request.method == "POST":
        name = request.POST.get('username')
        pass_wd = request.POST.get('userpass')
        if not name:
            return render(request, 'user/login.html', {'text': '请输入用户名'})
        if not pass_wd:
            return render(request, 'user/login.html', {'text': '请输入密码', 'name': name})
        try:
            yh = User.objects.get(u_name=name)
        except:
            return render(request, 'user/login.html', {'text': '用户名或密码错误', 'name': name})
        if yh.u_pass != pass_wd:
            return render(request, 'user/login.html', {'text': '用户名或密码错误', 'name': name})
        if request.session.get('ip', 0):
            return render(request, 'user/login.html', {'text': '用户名以登陆', 'name': name})
        request.session['ip'] = request.META['REMOTE_ADDR']
        request.session['u_name'] = yh.u_name
        request.session['u_id'] = yh.id
        return HttpResponseRedirect('/user/grzy')


def get_email_view(request):
    if request.method == "GET":
        email = request.GET.get('email')
        if not email:
            return HttpResponse('没有该邮箱')
        if User.objects.filter(u_email=email):
            return HttpResponse('邮箱以注册')
        email_list = []
        [i for i in range(6) if email_list.append(str(random.randint(0, 9)))]
        yzm = ''.join(email_list)
        try:
            mail.send_mail(
                subject='AID1907网络游戏厅注册',  # 题目
                message=yzm,  # 消息内容
                from_email='2865756660@qq.com',  # 发送者[当前配置邮箱]
                recipient_list=[email],  # 接收者邮件列表
            )
        except Exception as e:
            return HttpResponse('请输入正确的邮箱')
        request.session['email'] = email
        request.session['yzm'] = yzm
        return HttpResponse('ok')


def register_view(request):
    """
    注册视图
    :param request:
    :return:
    """
    if request.method == "GET":

        return render(request, 'user/register.html')
    elif request.method == "POST":
        name = request.POST.get('username')
        pass_wd1 = request.POST.get('password1')
        pass_wd2 = request.POST.get('password2')
        email = request.POST.get('email')
        yzm = request.POST.get('yzm')
        if not name:
            return render(request, 'user/register.html', {'text': '请输入用户名'})
        elif name.find(' ') >= 0:
            return render(request, 'user/register.html', {'text': '名字不允许有空格'})

        elif User.objects.filter(u_name=name):
            return render(request, 'user/register.html', {'text': '此用户以经被注册'})
        elif not email:
            return render(request, 'user/register.html', {'text': '邮箱不允许有空格'})
        elif not yzm:
            return render(request, 'user/register.html', {'text': '验证码不允许有空格'})
        elif not pass_wd1:
            return render(request, 'user/register.html', {'text': '请输入密码', 'name': name})
        elif pass_wd1.find(' ') >= 0:
            return render(request, 'user/register.html', {'text': '密码不允许有空格'})
        elif not pass_wd2:
            return render(request, 'user/register.html', {'text': '请输入核对密码', 'name': name})
        elif pass_wd1 != pass_wd2:
            return render(request, 'user/register.html', {'text': '密码不一致', 'name': name})
        elif request.session.get('email') != email or request.session.get('yzm') != yzm:
            return render(request, 'user/register.html', {'text': '验证码错误', 'name': name})
        try:
            User.objects.create(u_name=name, u_pass=pass_wd1, u_email=email)
        except:
            render(request, 'user/register.html', {'text': '此用户以经被注册'})
        request.session['u_name'] = name
        request.session['u_id'] = User.objects.get(u_name=name).id
        return HttpResponseRedirect('/user/grzy')


def grzy_view(request):
    if request.method == 'GET':
        try:
            user = User.objects.get(id=request.session['u_id'])
            vip = user.u_vip
        except Exception as e:
            print(e)
            return HttpResponse('请登录')
        return render(request, 'user/grzy.html', locals())


def get_xx_view(request):
    if request.method == "GET":
        username = request.GET.get('username')
        if not username:
            return HttpResponse('请输入用户名')
        try:
            User.objects.get(u_name=username)
        except:
            return HttpResponse('该用户名可用')
        return HttpResponse('用户名已被注册')





