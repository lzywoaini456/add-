from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(VideoType)
admin.site.register(Video)
admin.site.register(VideoComment)
admin.site.register(Likes)
