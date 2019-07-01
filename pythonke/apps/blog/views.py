from django.http import HttpResponse
from django.shortcuts import render


def post_create(request):
    return HttpResponse("create")

def post_detail(request):
    return HttpResponse("detail")

def post_list(request):
    return render(request, 'blog/list.html', {})

def post_update(request):
    return HttpResponse("update")

def post_delete(request):
    return HttpResponse("delete")