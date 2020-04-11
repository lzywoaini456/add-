from django.conf.urls import url
from . import views
urlpatterns = [
    url(r"^wan$", views.wan),
    url(r"^get_xx$", views.gat_xx),
    url(r"^fs_xx$", views.fs_xx),
]
