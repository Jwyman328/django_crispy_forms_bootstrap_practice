# from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, CreateView, ListView
from .models import Mailing_list_model, Create_blog_model


# Create your views here.


class Homepage_view(TemplateView):

    template_name = 'home.html'


class Mail_list_page_view(CreateView):
    model = Mailing_list_model
    template_name = 'mailing_list.html'
    fields = "__all__"




class All_blogs_page_view(ListView):
    template_name = 'all_blogs.html'
    model = Create_blog_model
    fields = "__all__"


class Createpage_view(CreateView):
    model = Create_blog_model
    template_name = 'create_blog.html'
    fields = "__all__"



class Aboutpage_view(TemplateView):
    template_name = 'about.html'


class Postpage_view(DetailView):
    model = Create_blog_model
    template_name = 'post.html'


