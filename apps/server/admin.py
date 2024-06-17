from django.contrib import admin

from .models import Usuario, Rank, APIKey

# Register your models here.
admin.site.register(Rank)
admin.site.register(APIKey)
admin.site.register(Usuario)