from django.db import models

# Create your models here.
class OrganizeDepart(models.Model):
    organizeid = models.IntegerField()
    name = models.CharField(max_length=20)

    class Meta:
        db_table = "organizedepart"

    def dict(self):
        organizedepart = {
            "id":self.id,
            "organizeid":self.organizeid,
            "name":self.name
        }
        return organizedepart