from django.shortcuts import render
from django.utils import timezone       # 게시글을 게시일로 정렬할려면 timezone 필요
from django.shortcuts import render, get_object_or_404    # 뷰 추가

from .models import Post                # .은 현재 디렉토리



def post_list(request):                # view function은 항상 첫번째 인자로 request를 갖는다
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})           # {}안에 매개변수 추가


def post_detail(request, pk):         # view 새부 페이지
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})