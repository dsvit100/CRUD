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
    
    # 여기서부터 
    post = Post()
    post.title = title
    post.content = content
    post.save() # 여기까지가 뭔소린지 모르겠음

    # return redirect('/index/') # 작성 및 저장 후 보여줄 경로
    return redirect(f'/posts/{post.id}/')