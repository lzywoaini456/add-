"""
    用户路由
"""
from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.favicon_ico),
    url(r'^index$', views.index_view),
    url(r'^add$', views.add_view),
    url(r'^get_sp$', views.get_sp_view),
    # url(r'^get_spp$', views.get_spp_view),
    url(r'^get_pl$', views.get_pl_view),
    url(r'^set_pl$', views.write_pl_view),
    url(r'^set_dz$', views.get_dz_view),
]
