from django.shortcuts import render
from django.utils import timezone
from .import models


def post_list(request):
    posts = models.Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'root/post_list.html', {'posts': posts})
