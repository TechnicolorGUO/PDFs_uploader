from django.db import models


class PDF(models.Model):
   files = models.FileField(upload_to='pdfs/')
