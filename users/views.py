from django.shortcuts import render, redirect, get_object_or_404
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from posts.models import Post

def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f"Account has been created for {username}.")
            return redirect("login")
    else:
        form = UserRegisterForm()
    return render(request, "users/register.html", {"form": form})


@login_required
def profile(request, username):
    profile_user = get_object_or_404(User, username=username)
    # Get posts for the profile_user (the user whose profile is being viewed)
    posts = Post.objects.filter(user=profile_user).order_by('-created_at')
    
    return render(request, 'users/profile.html', {
        'profile_user': profile_user,
        'posts': posts,  
        'user': request.user,  
    })


@login_required
def profile_update(request,username):
    """Handle profile updates on a separate page"""

    # logged-in user is updating their own profile
    if request.user.username != username:
        messages.error(request, "You can't update another user's profile!")
        return redirect('profile', username=request.user.username)
    
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your profile has been updated!')
            return redirect('profile', username=request.user.username) 
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    
    context = {
        'u_form': u_form,
        'p_form': p_form,
    }
    return render(request, 'users/profile_update.html', context)




 