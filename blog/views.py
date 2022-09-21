from django.shortcuts import render

posts = [
    {
        'author': 'Jon Doe',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'September 7, 2022'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'October 3, 2022'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html')
