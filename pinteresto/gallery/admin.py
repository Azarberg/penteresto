from django.contrib import admin

from .models import Category, News, Views, Likes, Tegs

admin.site.register(Category)
admin.site.register(News)
admin.site.register(Views)
admin.site.register(Likes)
admin.site.register(Tegs)
