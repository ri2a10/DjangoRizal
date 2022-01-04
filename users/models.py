from django.db import models

from django.contrib.auth.models import User

# Create your models here.

class Biodata(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nama = models.CharField(max_length=100)
    telp = models.CharField(max_length=16, blank=True, null=True)
    alamat = models.TextField(blank=True, null=True)

    def _str_(self):
        return "{}".format(self.nama)
    

    class Meta:
        verbose_name_plural = "Biodata"
