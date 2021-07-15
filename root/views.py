from django.shortcuts import render


def post_list(request):
    return render(request, 'root/post_list.html', {})
