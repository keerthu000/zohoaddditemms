# Generated by Django 4.1.7 on 2023-06-27 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zohoapp', '0018_additem_tax'),
    ]

    operations = [
        migrations.AddField(
            model_name='additem',
            name='invacc',
            field=models.TextField(max_length=255, null=True),
        ),
    ]
