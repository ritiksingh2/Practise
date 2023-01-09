from django.db import models



class Student_Admission(models.Model):
    student_id = models.CharField('Student ID',max_length=200)
    student_age = models.IntegerField('Student Age')
    student_name = models.CharField('Student Name',max_length=150)
    student_email = models.EmailField('Student Email')
    student_amount = models.FloatField('Student Amount')
    student_address = models.TextField('Student Address')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    college=models.ForeignKey('College',null=True,on_delete=models.CASCADE)

    
class College(models.Model):
    college_id = models.IntegerField('College ID')
    college_name = models.CharField('College Name',max_length=300)
    college_address = models.CharField('College Address',max_length=550)
    


    

