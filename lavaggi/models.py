from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse


class Lavaggio(models.Model):
    numero = models.CharField(max_length=255)
    kpi = models.TextField()
    video_lavaggio = models.FileField(upload_to="store_wash/")
    esito = models.CharField(max_length=255)
    data_lavaggio = models.DateTimeField(auto_now_add=True)
    utente = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.numero

    def get_absolute_url(self):
        return reverse('lavaggio_detail', args=[str(self.id)])
