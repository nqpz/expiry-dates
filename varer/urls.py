from django.urls import path
from django.conf import settings

from . import views

app_name = "varer"
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:varegruppe_id>", views.index_with_id, name="index_with_id"),
    path("varer/<int:vare_id>/opdater/", views.opdater, name="opdater")
]

if settings.DEBUG:
    urlpatterns.append(path("upload/<filename>", views.upload, name="upload"))
