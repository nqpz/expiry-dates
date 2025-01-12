from django.urls import path
from django.views.decorators.csrf import ensure_csrf_cookie

from . import views

app_name = "varer"
urlpatterns = [
    path("", ensure_csrf_cookie(views.IndexView.as_view()), name="index"),
    path("upload/<filename>", views.upload, name="upload"),
    path("upload/<filename>/thumbnail", views.upload_thumbnail, name="upload_thumbnail"),
    path("varer/ny/", views.ny, name="ny"),
    path("varer/ny/opret/", views.ny_opret, name="ny_opret"),
    path("varer/<int:vare_id>/opdater/", views.opdater, name="opdater")
]
