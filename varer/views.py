import os.path
from django.forms import ModelForm
from django.http import JsonResponse, HttpResponseRedirect, FileResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.conf import settings
from django.views.decorators.csrf import ensure_csrf_cookie
from sorl.thumbnail import get_thumbnail

from .models import Varegruppe, Vare

base = os.path.join(os.path.dirname(__file__), "..")

class IndexView(generic.ListView):
    template_name = "varer/index.html"
    context_object_name = "varer"

    def get_queryset(self):
        return Vare.objects.order_by("udløb_date")

class AndetVaregruppe:
    id = 0
    varegruppe_text = 'Andet'

def _index(request, varegruppe_id):
    varegrupper = list(Varegruppe.objects.order_by("varegruppe_text"))
    varegrupper.append(AndetVaregruppe())
    varer = Vare.objects.order_by("udløb_date")
    context = {
        "varegrupper": varegrupper,
        "varegruppe_id": varegruppe_id,
    }
    if varegruppe_id is None:
        context["varer"] = []
    elif varegruppe_id > 0:
        context["varer"] = varer.filter(varegruppe=varegruppe_id)
    else:
        context["varer"] = varer.filter(varegruppe=None)
    return render(request, "varer/index.html", context)

@ensure_csrf_cookie
def index(request):
    return _index(request, None)

@ensure_csrf_cookie
def index_with_id(request, varegruppe_id):
    return _index(request, varegruppe_id)

def opdater(request, vare_id):
    vare = get_object_or_404(Vare, pk=vare_id)
    vare.udløb_date = request.POST["date"]
    vare.save();
    return JsonResponse({"success": True})

if settings.DEBUG:
    def upload(request, filename):
        path = os.path.join(base, "upload", filename)
        return FileResponse(open(path, "rb"))
