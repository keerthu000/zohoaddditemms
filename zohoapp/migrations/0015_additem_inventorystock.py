# Generated by Django 4.1.7 on 2023-06-21 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zohoapp', '0014_additem_hsn'),
    ]

    operations = [
        migrations.AddField(
            model_name='additem',
            name='inventorystock',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]