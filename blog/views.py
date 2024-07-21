from django.shortcuts import render,redirect
from django.http  import HttpResponse
from django.urls import reverse
from .models import Article
from django.http import Http404
from django.core.paginator import Paginator
from .forms import ContactForm
import logging
# demo data
# posts=[
#         {'id':1,'title':'First Article','content':'This is the first article'},
#         {'id':2,'title':'Second Article','content':'This is the second article'},
#         {'id':3,'title':'Third Article','content':'This is the third article'},
#         {'id':4,'title':'Fourth Article','content':'This is the fourth article'},
#         {'id':5,'title':'Fifth Article','content':'This is the fifth article'},
    
#     ]

# Create your views here.
def index(request):
    article_title='Latest Articles'
    try:
        posts=Article.objects.all()
        paginator=Paginator(posts,5)
        page_number=request.GET.get('page')
        page_obj=paginator.get_page(page_number)
        

    except Article.DoesNotExist:
        
        raise Http404("does not exist")
    return render(request,'blogs/index.html',{'article_title':article_title,'page_obj':page_obj})   

def detail(request,slug):
    # demo data
    # post=next((post for post in posts if post['id']==int(post_id)),None)
    try:    
        post=Article.objects.get(slug=slug)
        related_articles=Article.objects.filter(category_id=post.category_id).exclude(slug=slug)
    # tile='Detail Page'
    # logger=logging.getLogger('TESTING')
    # logger.debug(f"Post  is {post}")
    except Article.DoesNotExist:
        raise Http404("Article does not exist")
    return render(request,'blogs/detail.html',{"post":post,"related_articles": related_articles},)

def old_url_redirect(request):
    return redirect(reverse('blog:news_link_url'))

def new_url_view(request):
    return HttpResponse("this is new url")

def contact_views(request):

    if request.method=='POST':
        form=ContactForm(request.POST)
        name= request.POST.get('name')
        email=request.POST.get('email')
        message=request.POST.get('message')

        logger=logging.getLogger('TESTING')
        success_message='Thanks for contacting us'
        if form.is_valid():
           logger.debug(f"Form  is {form.cleaned_data['name']} {form.cleaned_data['email']} {form.cleaned_data['message']}")
           return render(request,'blogs/contact.html',{'form':form,'success_message':success_message})
        else:
            logger.debug(f"Form  is invalid")
        return render(request,'blogs/contact.html',{'form':form})
    return render(request,'blogs/contact.html')
