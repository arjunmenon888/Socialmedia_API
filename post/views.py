from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Post

def post_list(request):
   posts = Post.objects.all()
   user = request.user
   context = {
       'posts': posts,
       'user': user
   }
   return render(request,'home.html',context)

def like_post(request):
    user = request.user
    
    if request.method == 'POST':
        post_id = request.POST.get('post_id')
        post = Post.objects.get(id=post_id)

        if user in post.Likes.all():
            post.Likes.remove(request.user)
            post.Unlikes.add(request.user)
        else:
            post.Likes.add(request.user)
            post.Unlikes.remove(request.user)

    return redirect('post:post-list')

def post_detail(request,pk):
   post = get_object_or_404(Post,pk=pk)
   return render(request,'detail.html',{'post': post})
