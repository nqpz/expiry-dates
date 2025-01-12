from django.contrib import admin

from .models import Vare

class VareAdmin(admin.ModelAdmin):
    # fieldsets = [(None, {"fields": ["varenavn_text", "udløb_date"]})]
    list_display = ["varenavn_text", "udløb_date"]

admin.site.site_header = "Vareadministration"
admin.site.register(Vare, VareAdmin)
