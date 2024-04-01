from django.shortcuts import render
from django.utils import timezone       # 게시글을 게시일로 정렬할려면 timezone 필요
from .models import Post                # .은 현재 디렉토리


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})           # {}안에 매개변수 추가