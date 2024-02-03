from django.db import models
from django.contrib.auth.models import User

# Create your models here.


# Class for the applicants model
class Applicant(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=255, null=False)
    last_name = models.CharField(max_length=255, null=False)
    date_of_birth = models.DateField(null=False)
    email = models.EmailField(null=False)
    phone_number = models.IntegerField(null=False)
    address = models.CharField(max_length=255, null=False)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, db_column="user_id", null=False
    )

    def __str__(self):
        return self.first_name


# Class for the positions model
class Position(models.Model):
    id = models.AutoField(primary_key=True)
    job_title = models.CharField(max_length=255, null=False)
    job_description = models.TextField(null=False)
    requirements = models.TextField(null=False)
    pay = models.DecimalField(max_digits=10, decimal_places=2, null=False)

    def __str__(self):
        return self.job_title


# Class for the managers model
class Manager(models.Model):
    manager_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=255, null=False)
    last_name = models.CharField(max_length=255, null=False)
    email = models.EmailField(null=False)

    def __str__(self):
        return self.first_name


# Class for the applications model
class Application(models.Model):
    id = models.AutoField(primary_key=True)
    resume = models.FileField(null=False, upload_to="files/")
    cover_letter = models.FileField(null=False, upload_to="files/")
    date_submitted = models.DateField(null=False)
    status = models.CharField(max_length=255, default="In progress")
    position = models.ForeignKey(
        Position, on_delete=models.CASCADE, db_column="position_id", null=False
    )
    applicant = models.ForeignKey(
        Applicant, on_delete=models.CASCADE, db_column="applicant_id", null=False
    )
    reviewed_by_manager = models.ForeignKey(
        Manager,
        on_delete=models.CASCADE,
        db_column="reviewed_by_manager_id",
        default=1,
        null=False,
    )

    def __int__(self):
        return self.id


# This class is just used as a test
class Test(models.Model):
    id = models.AutoField(primary_key=True)
    resume = models.FileField(null=True, blank=True, upload_to="files/")
    applicant = models.ForeignKey(
        Applicant, on_delete=models.CASCADE, db_column="applicant_id", null=False
    )
    position = models.ForeignKey(
        Position, on_delete=models.CASCADE, db_column="position_id", null=False
    )
    reviewed_by_manager = models.ForeignKey(
        Manager,
        on_delete=models.CASCADE,
        db_column="reviewed_by_manager_id",
        default=1,
        null=False,
    )
