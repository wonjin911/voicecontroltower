from __future__ import unicode_literals

from django.db import models

# Create your models here.
class UploadFileModel(models.Model):
    #file = models.FileField(null=True)
    file = models.FileField(null=True, upload_to="upload")