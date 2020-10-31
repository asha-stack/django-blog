from django.shortcuts import render

posts = [
    {
        'author': 'Asha',
        'title': 'Blog Post',
        'content': 'First content',
        'date_posted': 'August 27, 2018'
    },
    {
        'author': 'jane',
        'title': 'Blog Post 2',
        'content': 'Second content',
        'date_posted': 'August 28, 2018'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'bout'})