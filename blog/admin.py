from django.contrib import admin

# Register your models here.
from .models import Post,About

admin.site.register(Post)
admin.site.register(About)