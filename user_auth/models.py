from django.db import models
from django.contrib.auth.models import User
#from academy import Level

class_options = (
    ('Choose', ''),
    (1, 'Jss1'),
    (2, 'Jss2'),
    (3, 'Jss3'),
    (4, 'Sss1'),
    (5, 'Sss2'),
    (6, 'Sss3'),
    (7, 'Graduate'),
    (8, 'Staff'),
)


class Biodata(models.Model):
    student_id = models.CharField(max_length=15, null=True, blank=True)
    surname = models.CharField(max_length=20, blank=True, null=True)
    other_names = models.CharField(max_length=50, blank=True, null=True)
    _clas = models.PositiveIntegerField(default=1, choices=class_options, verbose_name='class')
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=8, blank=True, null=True)
    city = models.CharField(max_length=15, blank=True, null=True)
    lga = models.CharField(max_length=50, blank=True, null=True)
    address = models.TextField(max_length=100, blank=True, null=True)
    phn = models.CharField(max_length=11, blank=True, null=True)
    dob = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)
    profile_pic = models.ImageField(upload_to='static/blog/profile_pictures', blank=True, null=True)
    cover_pic = models.ImageField(upload_to='static/blog/cover_pictures', blank=True, null=True)
    about_me = models.TextField(blank=True, null=True)
    facebook_page = models.URLField(blank=True, null=True)

    def delete(self, *args, **kwargs):
        self.profile_pic.delete()
        self.cover_pic.delete()
        super().delete(*args, **kwargs)

    def __str__(self):
        return self.surname + self.other_names


class Skill(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    skill = models.CharField(max_length=35)
    description=models.TextField()
    degree_of_perfection=models.ImageField()

