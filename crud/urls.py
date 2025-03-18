"""
URL configuration for crud project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from posts import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # Read()ALL
    path('index/', views.index),

    # Read(1)
    # posts라는 경로에 id가 들어올 것입니다.(id: 게시물의 고유넘버)
    path('posts/<int:id>/', views.detail),
    # 상세페이지 만들 것이기 때문에 = detail로 설정
    # posts/1/
    # posts/10/
    # posts/123/ 모두 path('posts/<int:id>') 가 처리해줌
    
    # Create
    path('posts/new/', views.new), # 데이터 받아오기(입력)
    path('posts/create/', views.create), # 데이터 저장하는 공간
    
    # delete
    # 같은 url에 다른 기능은 구현 X
    # 따라서 /delete/를 추가해주기
    path('posts/<int:id>/delete/', views.delete),
]
