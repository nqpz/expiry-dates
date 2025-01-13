from django.urls import path
from django.views.decorators.csrf import ensure_csrf_cookie

from . import views

app_name = "varer"
urlpatterns = [
    path("", ensure_csrf_cookie(views.IndexView.as_view()), name="index"),
    path("upload/<filename>", views.upload, name="upload"), # Only for local development
    path("upload/<filename>/thumbnail", views.upload_thumbnail, name="upload_thumbnail"),
    path("varer/<int:vare_id>/opdater/", views.opdater, name="opdater")
]
