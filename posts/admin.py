from django.contrib import admin
# 현재 내 위치에 있는 model 파일의 post 클래스 불러오기
from .models import Post

# Register your models here.

# 위에 불러온 class Post를 관리자페이지에 register(등록)하기
admin.site.register(Post)