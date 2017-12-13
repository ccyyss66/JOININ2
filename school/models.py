from django.db import models

# Create your models here.
class School(models.Model):
    name = models.CharField(max_length=100)
    universityid = models.IntegerField(null=False)

    class Meta:
        db_table = "school"

    def dict(self):
        school = {
            "id":self.id,
            "name":self.name,
            "universityid":self.universityid
        }
        return school