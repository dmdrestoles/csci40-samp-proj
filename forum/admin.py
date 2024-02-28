from django.contrib import admin

from .models import *

admin.site.register(ThreadCategory)
admin.site.register(Thread)
admin.site.register(Post)