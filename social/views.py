from django.shortcuts import render, redirect,get_object_or_404

from social.models import Relationship
from .models import Post 
from .models import Relationship, Profile
from .forms import UserRegisterForm,PostForm,ProfileUpdateForm, UserUpdateForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required 
# Create your views here.
def feed(request):
    posts = Post.objects.all()

    context = {'posts':posts}
    return render(request,'social/feed.html',context)

def register(request):
    if request.method =='POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request, f'Usuario {username} creado')
            return redirect('feed')
    else: 
        form = UserRegisterForm()
    context = {'form': form}
    return render(request,'social/register.html',context)

@login_required
def post(request):
    current_user = get_object_or_404 (User, pk=request.user.pk)
    if request.method =='POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit = False)
            post.user = current_user
            post.save()
            messages.success(request, 'Post enviado')
            return redirect('feed')
    else:
        form = PostForm()
    return render(request, 'social/post.html',{'form':form})


def profile(request, username=None):
    current_user=request.user
    if username and username != current_user.username:
        user = User.objects.get(username=username)
        posts = user.posts.all()
    else:
        posts = current_user.posts.all()
        user = current_user
    return render(request,'social/profile.html',{'user':user,'posts':posts})

def follow(request, username):
    current_user = request.user
    to_user = User.objects.get(username = username)
    to_user_id = to_user
    rel = Relationship(from_user = current_user, to_user = to_user_id)
    rel.save()
    messages.success(request, f'Following {username}')
    return redirect('feed')

def unfollow(request, username):
    current_user = request.user
    to_user = User.objects.get(username = username)
    to_user_id = to_user.id
    rel = Relationship.objects.filter(from_user=current_user.id, to_user=to_user_id).get()
    rel.delete()
    messages.success(request, f'You dont follow {username} anymore')
    return redirect('feed')

def delete(request, post_id):
    post = Post.objects.get(id = post_id)
    post.delete()
    messages.success(request, f'Post deleted')
    return redirect('feed')

###def edit(request):
    if request.method == 'POST':
      u_form = UserUpdateForm(request.POST,instance = request.user)  
      p_form = ProfileUpdateForm(request.POST, request.FILES, instance = request.user.profile)

      if u_form.is_valid() and p_form.is_valid():
          u_form.save()
          p_form.save()
          return redirect('feed')
    else:
        u_form = UserUpdateForm(instance = request.user)
        p_form = ProfileUpdateForm()
    
    context = {'u_form': u_form,'p_form':p_form}
    return render(request,'social/edit.html',context)
###

def edit(request):
    if request.method =='POST':
        u_form = UserUpdateForm(request.POST)
        p_form = ProfileUpdateForm(request.POST,request.FILES) 

        if u_form.is_valid():
            u_form.save(commit = False )
            p_form.save(commit = False )
            useract = User.objects.get(username = request.user.username)
            useract.username = u_form.cleaned_data['username']
            useract.save()
            userimg = Profile.objects.get(pk = request.user.profile.pk)
            userimg.image = p_form.cleaned_data['image']
            userimg.save()
            messages.success(request, f'Profile updated')
            return redirect('feed')
    else: 
        u_form = UserUpdateForm()
        p_form = ProfileUpdateForm()
    context = {'u_form': u_form,'p_form': p_form}
    return render(request,'social/edit.html',context)


