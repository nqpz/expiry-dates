from django.db import models

class Varegruppe(models.Model):
    varegruppe_text = models.CharField("gruppenavn", max_length=200)

    def __str__(self):
        return self.varegruppe_text

    class Meta:
        verbose_name_plural = "varegrupper"

class Vare(models.Model):
    varenavn_text = models.CharField("varenavn", max_length=200)
    udløb_date = models.DateField("udløbsdato", blank=True, null=True)
    vare_image = models.ImageField("billede", blank=True, null=True, upload_to="upload")
    varegruppe = models.ForeignKey(Varegruppe, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.varenavn_text

    class Meta:
        verbose_name_plural = "varer"
