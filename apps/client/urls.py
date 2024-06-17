from django.urls import path
from . import views

urlpatterns = [
    path('', view=views.index, name='index'),
    path('login/', view=views.fazer_login, name='login'),
    path('logout/', view=views.fazer_logout, name='logout'),
    path('homepage/', view=views.homepage, name='homepage'),
]
