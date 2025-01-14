from django.contrib import admin

from .models import Varegruppe, Vare

class VaregruppeAdmin(admin.ModelAdmin):
    list_display = ["varegruppe_text"]

class VareAdmin(admin.ModelAdmin):
    list_display = ["varenavn_text", "udløb_date", "varegruppe"]

admin.site.site_header = "Vareadministration"
admin.site.register(Varegruppe, VaregruppeAdmin)
admin.site.register(Vare, VareAdmin)
