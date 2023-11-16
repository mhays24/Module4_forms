from django.contrib import admin
from django.urls import path
import app.views

urlpatterns = [
     path('hey/', app.views.hey_you, name='hey_you'),
    path("", app.views.root, name="root"),
    path("add/", app.views.add, name="add"),
    path("admin/", admin.site.urls),
]
