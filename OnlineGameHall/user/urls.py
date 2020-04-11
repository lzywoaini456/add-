"""
    用户路由
"""
from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^index$', views.index_view),
    url(r'^login$', views.login_view),
    url(r'^register$', views.register_view),
    url(r'^get_email$', views.get_email_view),
    url(r'^get_xx$', views.get_xx_view),
    url(r'^grzy$', views.grzy_view)
]
