from django.db import models

# Create your models here.
class Organize(models.Model):
    name = models.CharField(max_length=30)
    universityid = models.IntegerField()
    schoolid = models.IntegerField()
    introduce = models.CharField(max_length=500,null=True)
    type = models.IntegerField(null=True)

    class Meta:
        db_table = "organize"

    def dict(self):
        organize = {
            "id": self.id,
            "name":self.name,
            "universityid":self.universityid,
            "schoolid":self.schoolid,
            "introduce":self.introduce,
            "type":self.type
        }
        return organize