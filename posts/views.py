from django.shortcuts import render
from .models import Post


# Create your views here.
def index(request):
    # post 클래스가 가지고 있는 모든 데이터를 다 가져와
    posts = Post.objects.all()

    context = {
        'posts': posts,
    }

    return render(request, 'index.html', context)