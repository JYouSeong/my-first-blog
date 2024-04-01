from django.contrib import admin
from .models import Post                # post 모델을 가져옴

admin.site.register(Post)               # 모델 등록