from django.db import models

# Create your models here.
class SchoolAdmin(models.Model):
    userid = models.IntegerField(null=False)
    schoolid = models.IntegerField(null=False)
    universityid = models.IntegerField(null=False)

    class Meta:
        db_table = "schoolmanagerinfo"

    def dict(self):
        schooladmin = {
            "id":self.id,
            "userid":self.userid,
            "schoolid":self.schoolid,
            "universityid":self.universityid
        }
        return schooladmin