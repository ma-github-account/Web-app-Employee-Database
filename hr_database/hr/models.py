from django.db import models


# Create your models here.

#class Status(models.TextChoices):
#    UNSTARTED = 'u', "Not started yet"
#    ONGOING = 'o', "Ongoing"
#    FINISHED = 'f', "Finished"
#
#
#class Task(models.Model):
#    name = models.CharField(verbose_name="Task name", max_length=65, unique=True)
#    status = models.CharField(verbose_name="Task status", max_length=1, choices=Status.choices)
#
#    def __str__(self):
#        return self.name



class Company_branch(models.TextChoices):
    Chicago = "Chicago"
    Amsterdam = "Amsterdam"
    Bucharest = "Bucharest"

class Level_of_english(models.TextChoices):
    Weak = "Weak"
    Communicative = "Communicative"
    Fluent = "Fluent"

class Employee(models.Model):

    employee_id = models.CharField(unique=True, max_length=70)

    first_name = models.CharField(max_length=70)
    last_name = models.CharField(max_length=70)

    company_branch = models.CharField(max_length=10, choices=Company_branch.choices)

    department = models.CharField(max_length=70)
    position = models.CharField(max_length=70)

    personal_phone = models.CharField(max_length=70)
    personal_mail = models.CharField(max_length=70)
    address = models.CharField(max_length=70)

    date_of_birth = models.CharField(max_length=70)
    nationality = models.CharField(max_length=70)

    photo = models.ImageField(blank=True, upload_to="employee_photos/%Y/%m/%d", default=None)

    level_of_english = models.CharField(max_length=20, choices=Level_of_english.choices)
    native_language = models.CharField(max_length=70)

    def __str__(self):
        return self.employee_id

    def get_absolute_url(self):
    
        return reverse('hr:employee_detail', args=[self.id])












