from django.shortcuts import render,redirect
from django.http  import HttpResponse
from django.urls import reverse

# Create your views here.
def index(request):
    article_title='Latest Articles'
    posts=[
        # {'id':1,'title':'First Article','content':'This is the first article'},
        # {'id':2,'title':'Second Article','content':'This is the second article'},
        # {'id':3,'title':'Third Article','content':'This is the third article'},
        # {'id':4,'title':'Fourth Article','content':'This is the fourth article'},
        # {'id':5,'title':'Fifth Article','content':'This is the fifth article'},
    
    ]
    return render(request,'blogs/index.html',{'article_title':article_title,'posts':posts})   

def detail(request,post_id):
    tile='Detail Page'
    return render(request,'blogs/detail.html')

def old_url_redirect(request):
    return redirect(reverse('blog:news_link_url'))

def new_url_view(request):
    return HttpResponse("this is new url")
