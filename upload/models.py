from __future__ import unicode_literals

from django.db import models

def get_upload_path(instance, filename):
    return os.path.join(
      "user_%d" % instance.owner.id, "car_%s" % instance.slug, filename)

# Create your models here.
class UploadFileModel(models.Model):
    #file = models.FileField(null=True)
    file_id = models.AutoField(primary_key=True)
    file = models.FileField(null=True, upload_to="upload/%s.amr" % file_id)
