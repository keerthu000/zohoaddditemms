# Generated by Django 4.1.7 on 2023-08-01 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zohoapp', '0031_remove_additem_stock_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='additem',
            name='rate',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='additem',
            name='status_stock',
            field=models.TextField(default='active'),
        ),
    ]
