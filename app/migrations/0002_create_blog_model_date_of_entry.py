# Generated by Django 2.2.3 on 2019-07-10 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='create_blog_model',
            name='date_of_entry',
            field=models.DateField(null=True),
        ),
    ]
