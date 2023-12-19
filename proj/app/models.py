from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Products(models.Model):
    company = models.ForeignKey('Company', on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    price = models.IntegerField()

    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Students(models.Model):
    name = models.CharField(max_length=100)
    course = models.ManyToManyField('Course')

    def __str__(self):
        return self.name


class Course2(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Students2(models.Model):
    name = models.CharField(max_length=100)
    course = models.ManyToManyField('Course2', through='Enrollment')

    def __str__(self):
        return self.name


class Enrollment(models.Model):
    student = models.ForeignKey(Students2, on_delete=models.CASCADE)
    course = models.ForeignKey(Course2, on_delete=models.CASCADE)
    date = models.DateField()
    mark = models.PositiveIntegerField()