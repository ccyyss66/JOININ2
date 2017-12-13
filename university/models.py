from django.db import models

# Create your models here.
class University(models.Model):
    name = models.CharField(max_length=100)
    acronym = models.CharField(max_length=20,null=True)

    class Meta:
        db_table = "university"

    def dict(self):
        university = {
            "id":self.id,
            "name":self.name,
            "acronym":self.acronym
        }
        return university