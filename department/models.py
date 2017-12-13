from django.db import models

# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=100)
    schoolid = models.IntegerField(null=False)
    universityid = models.IntegerField(null=False)

    class Meta:
        db_table = "department"

    def dict(self):
        deparment = {
            "id":self.id,
            "name":self.name,
            "schoolid":self.schoolid,
            "universityid":self.universityid
        }
        return deparment