from django.urls import path
from django.views.decorators.csrf import ensure_csrf_cookie
from django.conf import settings

from . import views

app_name = "varer"
urlpatterns = [
    path("", ensure_csrf_cookie(views.IndexView.as_view()), name="index"),
    path("varer/<int:vare_id>/opdater/", views.opdater, name="opdater")
]

if settings.DEBUG:
    urlpatterns.append(path("upload/<filename>", views.upload, name="upload"))
