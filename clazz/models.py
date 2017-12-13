from django.db import models

# Create your models here.
class Clazz(models.Model):
    name = models.CharField(max_length=100)
    majorid = models.IntegerField(null=False)
    departmentid = models.IntegerField(null=False)
    schoolid = models.IntegerField(null=False)
    universityid = models.IntegerField(null=False)

    class Meta:
        db_table = "class"

    def dict(self):
        clazz = {
            "id": self.id,
            "name": self.name,
            "majorid":self.majorid,
            "departmentid": self.departmentid,
            "schoolid": self.departmentid,
            "universityid": self.universityid
        }
        return clazz