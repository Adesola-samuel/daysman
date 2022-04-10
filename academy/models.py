from django.db import models
from django.contrib.auth.models import User
from user_auth.models import Biodata
from django.db.models import Max, Avg, Min, Sum

occu_options = (
    ('Choose', ''),
    ('Student', 'Student'),
    ('Teacher', 'Teacher'),
 )

term_options = (
    ('Choose', ''),
    ('First Term', 'First Term'),
    ('Second Term', 'Second Term'),
    ('Third Term', 'Third Term'),
)
class_options = (
    ('Choose', ''),
    ('Jss1', 'Jss1'),
    ('Jss2', 'Jss2'),
    ('Jss3', 'Jss3'),
    ('Sss1', 'Sss1'),
    ('Sss3', 'Sss2'),
    ('Sss3', 'Sss3'),
)


class Session(models.Model):
    session = models.CharField(max_length=10)

    def __str__(self):
        return self.session


class Term(models.Model):
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    term = models.CharField(max_length=15, choices=term_options)
    no_of_times_school_opened = models.PositiveIntegerField(default=0)
    def __str__(self):
        return str(self.session) +'('+str(self.term)+')'

class Subject(models.Model):
    subject = models.CharField(max_length=25)
    active = models.BooleanField(default=False)

    def __str__(self):
        return str(self.subject)

class Clas(models.Model):
    clas = models.CharField(max_length=10, verbose_name='class')
    class_teacher = models.ForeignKey(Biodata,on_delete=models.CASCADE, null=True, blank=True)
    subjects = models.ManyToManyField(Subject, blank=True)
    def __str__(self):
        return self.clas

class Level(models.Model):
     term = models.ForeignKey(Term, on_delete = models.CASCADE)
     level = models.ForeignKey(Clas, on_delete = models.CASCADE)
     def __str__(self):
         return str(self.term) +' '+ str(self.level)

class StudentProgress(models.Model):
    user = models.ForeignKey(Biodata, on_delete=models.CASCADE, null=True, blank=True)
    clas = models.ForeignKey(Clas, on_delete=models.CASCADE, default=1, verbose_name='class')
    def __str__(self):
        return str(self.user) +''+ str(self.clas)

class Score(models.Model):
    student = models.ForeignKey(Biodata, on_delete=models.CASCADE)
    first_test = models.PositiveIntegerField(default=0)
    second_test = models.PositiveIntegerField(default=0)
    third_test = models.PositiveIntegerField(default=0)
    examination = models.PositiveIntegerField(default=0)
    level= models.ForeignKey(Level, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    def __str__(self):
        return '{} {}'.format(self.student.surname,self.student.other_names)

    @property
    def total_score(self):
        return self.first_test+self.second_test+self.third_test+self.examination

    @property
    def cont_ass(self):
        return self.first_test + self.second_test + self.third_test

    class Meta:
        ordering = ['level', 'subject']
        constraints = [
            models.UniqueConstraint(fields=['level', 'student', 'subject'], name='Student cannot have a double record of the same subject at the same level')
        ]

class StudentTermlyProfile(models.Model):
    student = models.ForeignKey(Biodata, on_delete=models.CASCADE)
    level = models.ForeignKey(Level, on_delete=models.CASCADE)
    comment_from_the_teacher = models.TextField(blank=True, null=True)
    comment_from_the_principal = models.TextField(blank=True, null=True)
    promoted = models.BooleanField(default=True, blank=True, null=True)
    no_present = models.PositiveIntegerField(default=128)
    no_open = models.PositiveIntegerField(default=128)

    @property
    def no_absent(self):
        return self.no_open - self.no_present

    def __str__(self):
        return '{} {}'.format(self.student.surname, self.student.other_names)