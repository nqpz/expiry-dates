from django.db import models

class Vare(models.Model):
    varenavn_text = models.CharField("varenavn", max_length=200)
    udløb_date = models.DateField("udløbsdato", blank=True)
    vare_image = models.ImageField("billede", blank=True, null=True, upload_to="upload")

    def __str__(self):
        return self.varenavn_text

    class Meta:
        verbose_name_plural = "varer"
