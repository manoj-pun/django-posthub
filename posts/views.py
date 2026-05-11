from django.shortcuts import render,redirect
from .models import Post
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .forms import PostForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def feeds(request):
    posts = Post.objects.all().order_by('-created_at')
    context = {
        "posts": posts
    }
    return render(request, "posts/feeds.html", context)


def home(request):
    return render(request, "posts/home.html")


@login_required
def upload_post(request,username):
    #logged-in user is uploading to their own profile
    if request.user.username != username:
        messages.error(request, "You can't upload posts to another user's profile!")
        return redirect('profile', username=request.user.username)
    
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            messages.success(request, 'Your post has been uploaded successfully!')
            return redirect('profile', username=request.user.username)
    else:
        form = PostForm()
    
    return render(request, 'posts/upload_post.html', {'form': form})



