from django.db import models

LANGUAGE_CHOICES = (('English', 'English'), ('Japanese', 'Japanese'), ('chinese', 'chinese'),
                    ('vietnamese', 'vietnamese'), ('Indonesia', 'Indonesia'), ('arabic', 'arabic'),
                    ('Bengal', 'Bengal'), ('german', 'german'), ('spanish', 'spanish'), ('french', 'french'),
                    ('Hindi', 'Hindi'), ('italian', 'italian'), ('malaysian', 'malaysian'), ('dutch', 'dutch'),
                    ('portukal ', 'portukal '), ('russian', 'russian'), ('thai', 'thai'), ('turkish', 'turkish'))


# Create your models here.
class Project(models.Model):
    image = models.ImageField(upload_to='project/', null=False)
    l_title = models.CharField(choices=LANGUAGE_CHOICES, max_length=20, null=False, blank=False)
    description = models.CharField(max_length=200, null=True)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.l_title
