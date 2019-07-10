from django.db import models
import datetime
from django.urls import reverse


# Create your models here.
class Mailing_list_model(models.Model):
    first_name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length = 100)
    date_of_birth = models.DateField()
    email = models.EmailField()
    additional_comments = models.TextField()

    def __str__(self):
        return self.email

    def get_absolute_url(self):
        return reverse('home')




class Create_blog_model(models.Model):
    title = models.CharField(max_length = 200)
    blog_text = models.TextField()
    date_of_entry = models.DateField(null=True)
    user = models.ForeignKey('auth.User', models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', args = [self.id] )


