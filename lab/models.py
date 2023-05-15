from django.db import models

__all__ = ['']


class Performance(models.Model):
    title = models.CharField(max_length=100, primary_key=True)
    author = models.CharField(max_length=100)
    genre = models.CharField(max_length=40)
    description = models.CharField(max_length=200, null=True, blank=True)


class Theater(models.Model):
    name = models.CharField(max_length=60, primary_key=True)
    address = models.CharField(max_length=100, null=True, blank=True)


class Employee(models.Model):
    SEX = [
        ("m", "male"),
        ("f", "female"),
    ]
    passport = models.CharField(max_length=100, primary_key=True)
    name = models.CharField(max_length=100)
    sex = models.CharField(max_length=1, choices=SEX)
    birthdate = models.DateField(null=True, blank=True)
    experience = models.PositiveIntegerField()
    position = models.CharField(max_length=40)
    theater = models.ManyToManyField(Theater)


class Director(models.Model):
    employee = models.OneToOneField(Employee, models.CASCADE, primary_key=True)
    theater = models.OneToOneField(Theater, models.CASCADE)


class Participant(models.Model):
    employee = models.OneToOneField(Employee, models.CASCADE, primary_key=True)


class Play(models.Model):
    participant = models.ForeignKey(Participant, models.CASCADE)
    performance = models.ForeignKey(Performance, models.CASCADE)
    theater = models.ForeignKey(Theater, models.CASCADE)


class Decorator(models.Model):
    participant = models.OneToOneField(Participant, models.CASCADE, primary_key=True)


class PlayDirector(models.Model):
    participant = models.OneToOneField(Participant, models.CASCADE, primary_key=True)


class Actor(models.Model):
    participant = models.OneToOneField(Participant, models.CASCADE, primary_key=True)


class Role(models.Model):
    TYPE = [
        ("main", "main"),
        ("sec", "secondary"),
    ]
    name = models.CharField(max_length=100, primary_key=True)
    actor = models.ForeignKey(Actor, models.CASCADE)
    performance_title = models.ForeignKey(Performance, models.CASCADE)
    type = models.CharField(max_length=4, choices=TYPE)

