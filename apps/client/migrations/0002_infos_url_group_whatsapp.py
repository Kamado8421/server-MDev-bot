# Generated by Django 5.0.2 on 2024-06-12 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='infos',
            name='url_group_whatsapp',
            field=models.URLField(default='https://wa.me/'),
        ),
    ]
