from django.db import models

# Create your models here.
# a foreign key is basically represented by an integer field which value is the primary key of the foreign object


class Student(models.Model):
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    date_admitted = models.DateTimeField(auto_now_add=True, null=True)
    class_admitted = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name


class Teacher(models.Model):
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    date_joined = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name


class Fees(models.Model):
    category = (
        ('Admission', 'Admission'),
        ('Monthly Fees', 'Monthly Fees'),
        ('Exam Fees', 'Exam Fees'),
        ('Other Fees', 'Other Fees'),
    )
    student = models.ForeignKey(Student, null=True, on_delete=models.SET_NULL)
    date_of_essue = models.DateTimeField(auto_now_add=True, null=True)
    fee_type = models.CharField(max_length=200, null=True, choices=category)
    amount = models.DecimalField(max_digits=10, decimal_places=2, null=True)

    def __str__(self):
        return self.fee_type
