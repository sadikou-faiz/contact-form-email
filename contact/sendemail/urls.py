
from django.contrib import admin
from django.urls import path , include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.contact_view, name='contact'),
     path('confirmation/',views.confirmation_view, name='confirmation'),
]
