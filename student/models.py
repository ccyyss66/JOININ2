from django.db import models

# Create your models here.
class StudentInfo(models.Model):
    userid = models.IntegerField()
    sex = models.IntegerField(null=True)
    workid = models.CharField(max_length=20,null=True)
    mobilephone = models.CharField(max_length=12,null=True)
    wechat = models.CharField(max_length=20,null=True)
    qq = models.CharField(max_length=20,null=True)
    universityid = models.IntegerField(null=True)
    schoolid = models.IntegerField(null=True)
    departmentid = models.IntegerField(null=True)
    majorid = models.IntegerField(null=True)
    classid = models.IntegerField(null=True)
    interest = models.CharField(max_length=200,null=True)
    state = models.IntegerField(null=True)

    class Meta:
        db_table = "studentinfo"

    def dict(self):
        studentInfo = {
            "id":self.id,
            "userid":self.userid,
            "sex":self.sex,
            "workid":self.workid,
            "mobilephone":self.mobilephone,
            "wechat":self.wechat,
            "qq":self.qq,
            "universityid":self.universityid,
            "schoolid":self.schoolid,
            "departmentid":self.departmentid,
            "majorid":self.majorid,
            "classid":self.classid,
            "interest":self.interest,
            "state":self.state
        }
        return studentInfo