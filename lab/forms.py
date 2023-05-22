from datetime import datetime, date

from django.core.exceptions import ValidationError
from django.forms import ModelForm
from django import forms
from django.utils.dateparse import parse_date

from lab.models import *

__all__ = ['PerformanceForm', 'TheaterForm', 'EmployeeForm', 'ParticipantForm', 'DirectorForm', 'DecoratorForm',
           'PlayDirectorForm', 'ActorForm', 'RoleForm', 'PutOnForm']


class PerformanceForm(ModelForm):
    error_css_class = 'error-field'
    required_css_class = 'required-field'

    class Meta:
        model = Performance
        fields = ['title', 'author', 'genre', 'description']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class': 'form-control mb-4'})
        self.fields['author'].widget.attrs.update({'class': 'form-control mb-4'})
        self.fields['genre'].widget.attrs.update({'class': 'form-control mb-4'})
        self.fields['description'].widget.attrs.update({'class': 'form-control mb-4', 'rows': '3'})


class TheaterForm(ModelForm):
    error_css_class = 'error-field'
    required_css_class = 'required-field'

    class Meta:
        model = Theater
        fields = ['name', 'address']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control mb-4'})
        self.fields['address'].widget.attrs.update({'class': 'form-control mb-4'})


class EmployeeForm(ModelForm):
    error_css_class = 'error-field'
    required_css_class = 'required-field'
    birthdate = forms.DateField(required=False)

    class Meta:
        model = Employee
        fields = ['passport', 'name', 'sex', 'birthdate', 'experience', 'position', 'theater']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['passport'].widget.attrs.update(
            {'class': 'form-control mb-4', 'Placeholder': '9 numbers or in format "XA 000000"'})
        self.fields['name'].widget.attrs.update({'class': 'form-control mb-4'})
        self.fields['sex'].widget.attrs.update({'class': 'form-control mb-4'})
        self.fields['birthdate'].widget.attrs.update({'class': 'form-control mb-4', 'Placeholder': 'YYYY-MM-DD'})
        self.fields['experience'].widget.attrs.update(
            {'class': 'form-control mb-4', 'Placeholder': 'Years of experience'})
        self.fields['position'].widget.attrs.update({'class': 'form-control mb-4'})
        self.fields['theater'].widget.attrs.update({'class': 'form-control mb-4'})

    def clean_birthdate(self):
        birthdate = self.cleaned_data.get('birthdate')
        print(birthdate)
        if birthdate is not None:
            if not date(1900, 1, 1) < birthdate < date.today():
                raise ValidationError('This date is invalid. Please, check it.')
        return birthdate

    def clean_passport(self):
        super(EmployeeForm, self).clean()
        passport = self.cleaned_data.get('passport')
        if len(passport) != 9:
            self._errors['passport'] = self.error_class([
                'Passport is invalid. Please, check it.'])
        if passport.find(' ') != -1:
            div = passport.split(' ')
            if len(div[0]) != 2 or div[0].isalpha() == False:
                self._errors['passport'] = self.error_class([
                    'Passport is invalid. Please, check it.'])
            if len(div[1]) != 6 or div[1].isnumeric() == False:
                self._errors['passport'] = self.error_class([
                    'Passport is invalid. Please, check it.'])
        else:
            if passport.isnumeric() == False:
                self._errors['passport'] = self.error_class([
                    'Passport is invalid. Please, check it.'])
        return passport


class ParticipantForm(ModelForm):
    error_css_class = 'error-field'
    required_css_class = 'required-field'

    class Meta:
        model = Participant
        fields = ['employee']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['employee'].widget.attrs.update({'class': 'form-control mb-4'})


class DirectorForm(ModelForm):
    error_css_class = 'error-field'
    required_css_class = 'required-field'

    class Meta:
        model = Director
        fields = ['employee', 'theater']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['employee'].widget.attrs.update({'class': 'form-control mb-4'})
        self.fields['theater'].widget.attrs.update({'class': 'form-control mb-4'})


class DecoratorForm(ModelForm):
    error_css_class = 'error-field'
    required_css_class = 'required-field'

    class Meta:
        model = Decorator
        fields = ['participant']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['participant'].widget.attrs.update({'class': 'form-control mb-4'})


class PlayDirectorForm(ModelForm):
    error_css_class = 'error-field'
    required_css_class = 'required-field'

    class Meta:
        model = PlayDirector
        fields = ['participant']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['participant'].widget.attrs.update({'class': 'form-control mb-4'})


class ActorForm(ModelForm):
    error_css_class = 'error-field'
    required_css_class = 'required-field'

    class Meta:
        model = Actor
        fields = ['participant']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['participant'].widget.attrs.update({'class': 'form-control mb-4'})


class RoleForm(ModelForm):
    error_css_class = 'error-field'
    required_css_class = 'required-field'

    class Meta:
        model = Role
        fields = ['name', 'type', 'performance_title', 'actor']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control mb-4'})
        self.fields['type'].widget.attrs.update({'class': 'form-control mb-4'})
        self.fields['performance_title'].widget.attrs.update({'class': 'form-control mb-4'})
        self.fields['actor'].widget.attrs.update({'class': 'form-control mb-4'})


class PutOnForm(ModelForm):
    error_css_class = 'error-field'
    required_css_class = 'required-field'

    class Meta:
        model = PutOn
        fields = ['theater', 'performance', 'participant']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['theater'].widget.attrs.update({'class': 'form-control mb-4'})
        self.fields['performance'].widget.attrs.update({'class': 'form-control mb-4'})
        self.fields['participant'].widget.attrs.update({'class': 'form-control mb-4'})

