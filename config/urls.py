from django.contrib import admin
from django.urls import path
import app.views

urlpatterns = [
    path("hey/", app.views.hey_you, name="hey_you"),
    path("age_in/", app.views.age_in, name="age_in"),
    path("order_total/", app.views.order_total, name="order_total"),
    path("admin/", admin.site.urls),
]
