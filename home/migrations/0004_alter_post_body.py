# Generated by Django 4.0.4 on 2022-07-09 00:14

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_post_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='body',
            field=tinymce.models.HTMLField(default='Mr. Anderson is working on this one.'),
        ),
    ]
