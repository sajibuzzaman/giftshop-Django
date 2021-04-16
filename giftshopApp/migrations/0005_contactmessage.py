# Generated by Django 3.2 on 2021-04-14 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('giftshopApp', '0004_about_team'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=40)),
                ('message', models.TextField(blank=True, max_length=1000)),
                ('status', models.CharField(choices=[('New', 'New'), ('Read', 'Read'), ('Closed', 'Closed')], default='New', max_length=40)),
                ('ip', models.CharField(blank=True, max_length=100)),
                ('Note', models.CharField(blank=True, max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
