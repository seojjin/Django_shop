from django.shortcuts import render
from shop.models import Item
from shop.models import Comment

# Create your views here.

def homepage(request):
    recent_items = Item.objects.order_by('-pk')[:3]
    return render(request, 'single_pages/homepage.html', {
        'recent_items': recent_items,
    })

def mypage(request):
    my_comments = Comment.objects.filter(author=request.user)
    my_likes = Item.objects.filter(like=request.user)
    return render(request, 'single_pages/mypage.html', {
        'my_comments': my_comments,
        'my_likes': my_likes,
    })


def companypage(request):
    return render(request,'single_pages/companypage.html')
