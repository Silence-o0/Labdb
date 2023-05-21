from datetime import datetime, date

from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator
from django.db import models

__all__ = ['Performance', 'Theater', 'Employee', 'Director', 'Participant', 'PutOn', 'Decorator', 'PlayDirector',
           'Actor', 'Role']


class Performance(models.Model):
    title = models.CharField(max_length=100, primary_key=True)
    author = models.CharField(max_length=100)
    genre = models.CharField(max_length=40)
    description = models.CharField(max_length=300, null=True, blank=True)

    def __str__(self):
        return str(self.title)


class Theater(models.Model):
    name = models.CharField(max_length=100, primary_key=True)
    address = models.CharField(max_length=120, null=True, blank=True)

    def __str__(self):
        return str(self.name)


class Employee(models.Model):
    SEX = [
        ("male", "male"),
        ("female", "female"),
    ]
    passport = models.CharField(max_length=100, primary_key=True)
    name = models.CharField(max_length=100)
    sex = models.CharField(max_length=6, choices=SEX)
    birthdate = models.DateField(null=True, blank=True)
    experience = models.PositiveIntegerField(validators=[
            MaxValueValidator(100)
        ])
    position = models.CharField(max_length=40)
    theater = models.ManyToManyField(Theater, blank=True)

    def __str__(self):
        return str(self.name)


class Director(models.Model):
    employee = models.OneToOneField(Employee, models.CASCADE, primary_key=True)
    theater = models.OneToOneField(Theater, models.CASCADE)

    def __str__(self):
        return f'{self.theater} {self.employee}'


class Participant(models.Model):
    employee = models.OneToOneField(Employee, models.CASCADE, primary_key=True)

    def __str__(self):
        return str(self.employee)


class PutOn(models.Model):
    participant = models.ForeignKey(Participant, models.CASCADE)
    performance = models.ForeignKey(Performance, models.CASCADE)
    theater = models.ForeignKey(Theater, models.CASCADE)

    def __str__(self):
        return f'theater:{self.theater} / performance:{self.performance} / participant: {self.participant} '


class Decorator(models.Model):
    participant = models.OneToOneField(Participant, models.CASCADE, primary_key=True)

    def __str__(self):
        return str(self.participant)


class PlayDirector(models.Model):
    participant = models.OneToOneField(Participant, models.CASCADE, primary_key=True)

    def __str__(self):
        return str(self.participant)


class Actor(models.Model):
    participant = models.OneToOneField(Participant, models.CASCADE, primary_key=True)

    def __str__(self):
        return str(self.participant)


class Role(models.Model):
    TYPE = [
        ("main", "main"),
        ("secondary", "secondary"),
    ]
    name = models.CharField(max_length=100, primary_key=True)
    actor = models.ForeignKey(Actor, models.CASCADE)
    performance_title = models.ForeignKey(Performance, models.CASCADE)
    type = models.CharField(max_length=9, choices=TYPE)

    def __str__(self):
        return f'"{self.performance_title}": {self.name}'
