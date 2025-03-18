from django.shortcuts import render, redirect
from .models import Post


# Create your views here.
def index(request):
    # post 클래스가 가지고 있는 모든 데이터를 다 가져와
    posts = Post.objects.all()
    context = {
        'posts': posts,
    }
    return render(request, 'index.html', context)

def detail(request, id):
    post = Post.objects.get(id=id) # id 컬럼의 id(숫자) 데이터를 찾아줘
    context = {
        'post': post,
    }
    return render(request, 'detail.html', context)

def new(request):
    return render(request, 'new.html')

def create(request):
    title = request.GET.get('title')
    content = request.GET.get('content')
    
    post = Post()
    post.title = title
    post.content = content
    # 파이썬 세상의 객체로만 존재
    # save를 해줘야 DB에 저장이 되며 고유번호가 생성됨
    post.save()

    # return redirect('/index/') # 작성 및 저장 후 보여줄 경로
    return redirect(f'/posts/{post.id}/')

def delete(request, id):
    # 삭제할 게시물 찾기
    post = Post.objects.get(id=id)
    post.delete()
    return redirect('/index/')