from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import PostForm

def post_create(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Successfully created", extra_tags='alert-success')
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        'form': form,
    }
    return render(request, 'blog/post_form.html', context)

def post_detail(request, pk=None):
    instance = get_object_or_404(Post, pk=pk)
    context = {
        'obj': instance
    }
    return render(request, 'blog/post_detail.html', context)

def post_list(request):
    queryset = Post.objects.all()
    context = {
        'object_list': queryset
    }
    return render(request, 'blog/list.html', context)

def post_update(request, pk=None):
    instance = get_object_or_404(Post, pk=pk)
    form = PostForm(request.POST or None, instance=instance)
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
    instance = get_object_or_404(Post, pk=pk)
    instance.delete()
    messages.success(request, "Successfully deleted", extra_tags='alert-success')
    return redirect('blog:list')