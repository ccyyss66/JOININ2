from django.db import models

# Create your models here.
class Major(models.Model):
    name = models.CharField(max_length=100)
    departmentid = models.IntegerField(null=False)
    schoolid = models.IntegerField(null=False)
    universityid = models.IntegerField(null=False)

    class Meta:
        db_table = "major"

    def dict(self):
        major = {
            "id":self.id,
            "name":self.name,
            "departmentid":self.departmentid,
            "schoolid":self.departmentid,
            "universityid":self.universityid
        }
        return major