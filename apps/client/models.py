from django.db import models

# Create your models here.
class Info(models.Model):
    admin = models.CharField(default='luhdev', null=False, blank=False, max_length=6, unique=True)
    url_youtube_admin = models.URLField(default='https://youtube.com', null=False, blank=False)
    url_instagram_admin = models.URLField(default='https://www.instagram.com/works_manager', null=False, blank=False)
    url_github_admin = models.URLField(default='https://github.com/Kamado8421/', null=False, blank=False)
    url_group_whatsapp = models.URLField(default='https://wa.me/', null=False, blank=False)


class ConfigBot(models.Model):
    prefix = models.CharField(max_length=1, null=False, blank=False, default='/')
    nomeBot = models.CharField(null=False, blank=False, max_length=35)
    nomeDono = models.CharField(null=False, blank=False, max_length=35)
    numeroBot = models .CharField(null=False, blank=False, max_length=35)
    numeroDono = models.CharField(null=False, blank=False, max_length=35)
    nomeDinheiro = models.CharField(null=False, blank=False, max_length=35)

    identificadorNomeBot = models.CharField(null=False, blank=False, max_length=35)

    def __str__(self):
        return f'{self.nomeBot} - ID-API: {self.identificadorNomeBot}'