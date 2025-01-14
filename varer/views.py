import os.path
from django.forms import ModelForm
from django.http import JsonResponse, HttpResponseRedirect, FileResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.conf import settings
from sorl.thumbnail import get_thumbnail

from .models import Vare

base = os.path.join(os.path.dirname(__file__), "..")

class IndexView(generic.ListView):
    template_name = "varer/index.html"
    context_object_name = "varer"

    def get_queryset(self):
        return Vare.objects.order_by("udløb_date")

def opdater(request, vare_id):
    vare = get_object_or_404(Vare, pk=vare_id)
    vare.udløb_date = request.POST["date"]
    vare.save();
    return JsonResponse({"success": True})

if settings.DEBUG:
    def upload(request, filename):
        path = os.path.join(base, "upload", filename)
        return FileResponse(open(path, "rb"))
