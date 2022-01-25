from django.db import models

# Create your models here.
branch_choice = (
    ('M.s.cs','M.s.cs'),
    ('M.p.cs','M.p.cs'),
    ('B.com','B.com'),
    ('B.z.c','B.z.c'),
)
qualification_choice =(
    ('MCA','MCA'),
    ('Mcom','Mcom'),
    ('B.Tech','B.Tech'),
    ('CA','CA'),
)
class studentmodel(models.Model):
    Name = models.CharField(max_length=30)
    Age = models.IntegerField()
    Mobile = models.IntegerField()
    Email = models.EmailField()
    Qualification = models.CharField(max_length=30,choices=qualification_choice)
    Branch = models.CharField(max_length=30,choices=branch_choice)
    class Meta :
        abstract = True
exam_choice = (
    ('Computer','Computer'),
    ('Non-Computer','Non-Computer'),
)
class detailmodel(studentmodel):
    Exam = models.CharField(max_length=30,choices=exam_choice)
examtype_choice = (
    ('Online','Online'),
    ('Offline','Offline'),
)
class exammodel(models.Model):
    Exam_Type = models.CharField(max_length=30,choices=examtype_choice)
    Time = models.TimeField()
    Feedback = models.TextField(default='Write Something For heare....')


