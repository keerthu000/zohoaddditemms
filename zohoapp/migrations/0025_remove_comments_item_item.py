# Generated by Django 4.1.7 on 2023-07-12 11:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zohoapp', '0024_rename_comments_comments_item'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comments_item',
            name='item',
        ),
    ]
