from django.views import generic
from django.shortcuts import render,redirect, HttpResponse, get_object_or_404
from .models import *
from django.contrib.auth.models import User
from .forms import *
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

#@user_passes_test(lambda u: u.is_superuser)
@login_required
def add_blog(request):
    
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            status=form.cleaned_data.get('status')
            post=form.save(commit=False)
            post.author= request.user
            post.save()
            return redirect("/blog")
    else:
        form=PostForm()
    return render(request, 'blog/blog_post.html', {'form':form})
           

def view_post(request, slug):
    post=get_object_or_404(Post, slug=slug)
    if request.method=="POST":
        form=CommentForm(request.POST)
        if form.is_valid():
            comment=form.save(commit=False)
            comment.post=post
            comment.save()
            return redirect(request.path)
    else:
        form=CommentForm()
    
    form.initial['name'] = request.session.get('name')
    form.initial['email'] = request.session.get('email')
    arg={'form':form, "post":post}
    return render(request, "blog/post_detail.html", arg)

def show(request):
    post1= Post.objects.filter(status=1).order_by('-created_on')
    page = request.GET.get('page', 1)

    paginator = Paginator(post1, 5)
    try:
        post2 = paginator.page(page)
    except PageNotAnInteger:
        post2 = paginator.page(1)
    except EmptyPage:
        post2 = paginator.page(paginator.num_pages)
    return render(request, "blog/index.html", {'post1':post1, 'post2':post2})