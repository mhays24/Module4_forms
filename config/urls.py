from django.contrib import admin
from django.urls import path
import app.views

urlpatterns = [
    path("", app.views.index, name="index"),
    path("hey/", app.views.hey_you, name="hey_you"),
    path("age_in/", app.views.age_in, name="age_in"),
    path("order_total/", app.views.order_total, name="order_total"),
    path("warmup-2/font_times/", app.views.font_times, name="font_times"),
    path("logic-2/no-teen-sum/", app.views.no_teen_sum, name="no_teen_sum"),
    path("string-2/xyz-there/", app.views.xyz_there, name="xyz_there"),
    path("list-2/centered-average/", app.views.centered_average, name="centered_average"),
    path("admin/", admin.site.urls),
]
