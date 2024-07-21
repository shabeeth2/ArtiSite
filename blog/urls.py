from django.urls import path  
from . import views

app_name='blog'
urlpatterns = [
    path("",views.index,name="index"),
    path("post/<str:slug>",views.detail,name="detail"),
    path("new_url",views.new_url_view,name="news_link_url"),
    path("old_url",views.old_url_redirect,name="old_url"),
    path("contact",views.contact_views,name="contact"),

]