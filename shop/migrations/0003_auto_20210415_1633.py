# Generated by Django 3.2 on 2021-04-15 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_category_parent'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='Properties',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='Styles',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='compositions',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
