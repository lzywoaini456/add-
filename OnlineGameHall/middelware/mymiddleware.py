"""
    中间件大全
"""
from django.shortcuts import render
from django.utils.deprecation import MiddlewareMixin


class MyMw(MiddlewareMixin):
    def process_request(self, request):
        # if request.path_info == '/user/login':
        #     return None
        # if not request.session.get('u_name', 0) and not request.session.get('u_id', 0):
        #     return render(request, 'user/login.html', {'text': '有人把你顶下来了'})
        return None
#     def process_view(self, request, callback, callback_args, callback_kwargs):
#         """
#         即将进入视图时调用
#         :param request: 请求
#         :param callback: 视图函数
#         :param callback_args: 位置传参
#         :param callback_kwargs: 关键字传参
#         :return: 同上
#         """
#         print('MyMw process_view do---')
#
#     def process_response(self, request, response):
#         """
#         响应给浏览器之前调用
#         :param request: 请求
#         :param response: 视图结果
#         :return: 必须返回 Http_response
#         """
#         print('MyMw process_response do---')
#         return response
#
#
# """
#     中间件大全二
# """
#
#
# class MyMw2(MiddlewareMixin):
#     # 到达主路由之前调用
#     def process_request(self, request):
#
#         print('MyMw2 process_request do ---')
#
#     def process_view(self, request, callback, callback_args, callback_kwargs):
#         """
#         即将进入视图时调用
#         :param request: 请求
#         :param callback: 视图函数
#         :param callback_args: 位置传参
#         :param callback_kwargs: 关键字传参
#         :return: 同上
#         """
#         print('MyMw2 process_view do---')
#
#     def process_response(self, request, response):
#         """
#         响应给浏览器之前调用
#         :param request: 请求
#         :param response: 视图结果
#         :return: 必须返回 Http_response
#         """
#         print('MyMw2 process_response do---')
#         return response
