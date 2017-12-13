from django.db import models

# Create your models here.
class AssociateInfo(models.Model):
    organizeid = models.IntegerField()
    organizedepartid = models.IntegerField()
    sno = models.IntegerField()
    state = models.IntegerField()
    auditsug = models.CharField(max_length=300,null=True)
    identity = models.IntegerField(null=True)

    class Meta:
        db_table = "associateinfo"

    def dict(self):
        associateinfo = {
            "id":self.id,
            "organizeid":self.organizeid,
            "organizedepartid":self.organizedepartid,
            "sno":self.sno,
            "state":self.state,
            "auditsug":self.auditsug,
            "identity":self.identity
        }
        return associateinfo