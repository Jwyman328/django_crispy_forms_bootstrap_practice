from django.contrib import admin
from .models import Create_blog_model, Mailing_list_model

# Register your models here.
admin.site.register(Create_blog_model)
admin.site.register(Mailing_list_model)
