# Generated by Django 5.0.2 on 2024-06-13 00:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0002_infos_url_group_whatsapp'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConfigBot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prefix', models.CharField(default='/', max_length=1)),
                ('nomeBot', models.CharField(max_length=35)),
                ('nomeDono', models.CharField(max_length=35)),
                ('numeroBot', models.CharField(max_length=35)),
                ('numeroDono', models.CharField(max_length=35)),
                ('nomeDinheiro', models.CharField(max_length=35)),
                ('identificadorNomeBot', models.CharField(max_length=35)),
            ],
        ),
    ]
