from django.db import models

# Create your models here.
class Image(models.Model):
    path = models.CharField(max_length=100,null=True)
    description = models.CharField(max_length=200,null=True)
    name = models.CharField(max_length=50,null=True)

    class Meta:
        db_table = "image"

    def dict(self):
        image = {
            "path":self.path,
            "description":self.description,
            "name":self.name
        }
        return image