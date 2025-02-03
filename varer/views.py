import os
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

def login(request):
    env = os.getenv("PASSWORD")
    if env and request.POST["password"] == env:
        del request.session['failed_to_login']
        request.session['logged_in'] = True
    else:
        request.session['failed_to_login'] = True
    return HttpResponseRedirect(reverse("varer:index"))

def _index(request, varegruppe_id):
    if 'logged_in' not in request.session:
        return render(request, "varer/login.html",
                      {"border_color": 'red' if 'failed_to_login' in request.session else 'black'})

    if varegruppe_id is None:
        varegruppe_actual = None
    else:
        varegruppe_actual = get_object_or_404(Varegruppe, pk=varegruppe_id)
    varegrupper = list(Varegruppe.objects.order_by("varegruppe_text"))
    varer = Vare.objects.order_by("udløb_date")
    context = {
        "varegrupper": varegrupper,
        "varegruppe_actual": varegruppe_actual,
    }
    if varegruppe_id is None:
        context["varer"] = []
    else:
        context["varer"] = varer.filter(varegruppe=varegruppe_id)
    return render(request, "varer/index.html", context)

@ensure_csrf_cookie
def index(request):
    return _index(request, None)

@ensure_csrf_cookie
def index_with_id(request, varegruppe_id):
    return _index(request, varegruppe_id)

def opdater(request, vare_id):
    vare = get_object_or_404(Vare, pk=vare_id)
    user_input = request.POST["date"]
    vare.udløb_date = None if user_input == '' else user_input
    vare.save();
    return JsonResponse({"success": True})

if settings.DEBUG:
    def upload(request, filename):
        path = os.path.join(base, "upload", filename)
        return FileResponse(open(path, "rb"))
