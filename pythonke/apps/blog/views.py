from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.utils import timezone
from .models import Post
from .forms import PostForm

def post_create(request):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404

    form = PostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()
        messages.success(request, "Successfully created", extra_tags='alert-success')
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        'form': form,
    }
    return render(request, 'blog/post_form.html', context)

def post_detail(request, pk=None):
    instance = get_object_or_404(Post, pk=pk)
    if instance.draft:
        if not request.user.is_staff or not request.user.is_superuser:
            raise Http404

    context = {
        'obj': instance
    }
    return render(request, 'blog/post_detail.html', context)

def post_list(request):
    post_list = Post.objects.active()
    if request.user.is_staff or request.user.is_superuser:
        post_list = Post.objects.all()
    paginator = Paginator(post_list, 5) # Show 25 contacts per page

    page = request.GET.get('page')
    queryset = paginator.get_page(page)

    context = {
        'object_list': queryset
    }
    return render(request, 'blog/list.html', context)

def post_update(request, pk=None):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404

    instance = get_object_or_404(Post, pk=pk)
    form = PostForm(request.POST or None, request.FILES or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Saved", extra_tags='alert-success')
        return HttpResponseRedirect(instance.get_absolute_url())

    context = {
        'obj': instance,
        'form': form
    }
    return render(request, 'blog/post_form.html', context)

def post_delete(request, pk=None):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404

    instance = get_object_or_404(Post, pk=pk)
    instance.delete()
    messages.success(request, "Successfully deleted", extra_tags='alert-success')
    return redirect('blog:list')