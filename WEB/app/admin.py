import django.contrib.admin
from django.contrib import admin

from app.models import Like, Profile, Tag, Question, Answer

# Register your models here.

admin.site.register(Profile)
admin.site.register(Tag)
admin.site.register(Like)
admin.site.register(Question)
admin.site.register(Answer)
