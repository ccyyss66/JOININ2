from django.db import models

# Create your models here.
class Communication(models.Model):
    userid = models.IntegerField(null=False)
    schoolid = models.IntegerField(null=True)
    state = models.IntegerField(null=False)
    activity = models.IntegerField(null=True)
    content = models.CharField(max_length=500,null=True)
    qq = models.CharField(max_length=15,null=True)
    wechat = models.CharField(max_length=30,null=True)
    phone = models.CharField(max_length=15,null=True)
    start = models.DateField(null=True)
    end = models.DateField(null=True)
    topic = models.CharField(max_length=50,null=True)

    class Meta:
        db_table = "communication"

    def dict(self):
        communication = {
            "id":self.id,
            "userid":self.userid,
            "schoolid":self.schoolid,
            "state":self.state,
            "activity":self.activity,
            "content":self.content,
            "qq":self.qq,
            "wechat":self.wechat,
            "phone":self.phone,
            "start":self.start,
            "end":self.end,
            "topic":self.topic
        }
        return communication