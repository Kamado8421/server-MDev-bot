from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('server/', include('apps.server.urls')),
    path('', include('apps.client.urls')),
]
