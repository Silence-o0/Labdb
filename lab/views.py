from django.contrib import messages
from django.core.exceptions import ValidationError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.template import loader

from .forms import *
from .models import *


# performances


def get_all_performances(request):
    performances = Performance.objects.all().values()
    template = loader.get_template('performances-table.html')
    context = {
        'performances': performances,
        'title': 'Performances',
    }
    return HttpResponse(template.render(context, request))


def add_performance(request):
    try:
        if request.method == "POST":
            form = PerformanceForm(request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                post.save()
                return redirect('/performances/')
        else:
            form = PerformanceForm()
        context = {
            'form': form,
            'title': 'Performances',
            'action': 'Add',
        }
        return render(request, 'add-edit.html', context=context)
    except():
        return HttpResponseRedirect('/performances/')


def edit_performance(request, title):
    try:
        performance = get_object_or_404(Performance, title=title)
        form = PerformanceForm(request.POST or None, instance=performance)
        if form.is_valid():
            if form['title'].value() != title:
                messages.error(request, 'You can not change title.')
                return redirect('edit-performance', title)
            else:
                form.save()
                return redirect('list-performances')
        context = {
            'form': form,
            'title': 'Performances',
            'action': 'Edit',
        }
        return render(request, 'add-edit.html', context)
    except():
        return HttpResponseRedirect('/performances/')


def delete_performance(request, title):
    performance = Performance.objects.get(title=title)
    performance.delete()
    return HttpResponseRedirect('/performances/')


# theaters


def get_all_theaters(request):
    theaters = Theater.objects.all().values()
    template = loader.get_template('theaters-table.html')
    context = {
        'theaters': theaters,
        'title': 'Theaters',
    }
    return HttpResponse(template.render(context, request))


def add_theater(request):
    try:
        if request.method == "POST":
            form = TheaterForm(request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                post.save()
                return redirect('/theaters/')
        else:
            form = TheaterForm()
        context = {
            'form': form,
            'title': 'Theaters',
            'action': 'Add',
        }
        return render(request, 'add-edit.html', context=context)
    except():
        return HttpResponseRedirect('/theaters/')


def edit_theater(request, name):
    try:
        theaters = get_object_or_404(Theater, name=name)
        form = TheaterForm(request.POST or None, instance=theaters)
        if form.is_valid():
            if form['name'].value() != name:
                messages.error(request, 'You can not change name.')
                return redirect('edit-theater', name)
            else:
                form.save()
                return redirect('list-theaters')
        context = {
            'form': form,
            'title': 'Theaters',
            'action': 'Edit',
        }
        return render(request, 'add-edit.html', context)
    except():
        return HttpResponseRedirect('/theaters/')


def delete_theater(request, name):
    theater = Theater.objects.get(name=name)
    theater.delete()
    return HttpResponseRedirect('/theaters/')


# employee


def get_all_employees(request):
    employees = Employee.objects.all()
    template = loader.get_template('employees-table.html')
    context = {
        'employees': employees,
        'title': 'Employees',
    }
    return HttpResponse(template.render(context, request))


def add_employee(request):
    try:
        if request.method == "POST":
            form = EmployeeForm(request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                post.save()
                return redirect('/employees/')
        else:
            form = EmployeeForm()
        context = {
            'form': form,
            'title': 'Employees',
            'action': 'Add',
        }
        return render(request, 'add-edit.html', context=context)
    except():
        return HttpResponseRedirect('/employees/')


def edit_employee(request, passport):
    try:
        employees = get_object_or_404(Employee, passport=passport)
        form = EmployeeForm(request.POST or None, instance=employees)
        if form.is_valid():
            if form['passport'].value() != passport:
                messages.error(request, 'You can not change passport.')
                return redirect('edit-employee', passport)
            else:
                form.save()
                return redirect('list-employees')
        context = {
            'form': form,
            'title': 'Employees',
            'action': 'Edit',
        }
        return render(request, 'add-edit.html', context)
    except():
        return HttpResponseRedirect('/employees/')


def delete_employee(request, passport):
    employee = Employee.objects.get(passport=passport)
    employee.delete()
    return HttpResponseRedirect('/employees/')


# participants


def get_all_participants(request):
    participants = Participant.objects.all().values()
    employee = Employee.objects.filter(passport__in=participants)
    template = loader.get_template('participants-table.html')
    context = {
        'participants': employee,
        'title': 'Participants',
    }
    return HttpResponse(template.render(context, request))


def add_participant(request):
    try:
        if request.method == "POST":
            form = ParticipantForm(request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                post.save()
                return redirect('/participants/')
        else:
            form = ParticipantForm()
        context = {
            'form': form,
            'title': 'Participants',
            'action': 'Add',
        }
        return render(request, 'add-edit.html', context=context)
    except():
        return HttpResponseRedirect('/participants/')


def delete_participant(request, employee_id):
    participant = Participant.objects.get(employee_id=employee_id)
    participant.delete()
    return HttpResponseRedirect('/participants/')


# directors


def get_all_directors(request):
    directors = Director.objects.all()
    template = loader.get_template('directors-table.html')
    context = {
        'directors': directors,
        'title': 'Directors',
    }
    return HttpResponse(template.render(context, request))


def add_director(request):
    try:
        if request.method == "POST":
            form = DirectorForm(request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                post.save()
                return HttpResponseRedirect('/directors/')
        else:
            form = DirectorForm()
        context = {
            'form': form,
            'title': 'Directors',
            'action': 'Add',
        }
        return render(request, 'add-edit.html', context=context)
    except():
        return HttpResponseRedirect('/directors/')


def edit_director(request, employee_id):
    directors = get_object_or_404(Director, employee_id=employee_id)
    form = DirectorForm(request.POST or None, instance=directors)
    try:
        if form.is_valid():
            if form['employee'].value() != employee_id:
                messages.error(request, 'You can not change employee. But you can delete him.')
                return redirect('edit-director', employee_id)
            else:
                form.save()
                return redirect('list-directors')
        context = {
            'form': form,
            'title': 'Directors',
            'action': 'Edit',
        }
        return render(request, 'add-edit.html', context)
    except():
        return redirect('list-directors')


def delete_director(request, employee_id):
    director = Director.objects.get(employee_id=employee_id)
    director.delete()
    return HttpResponseRedirect('/directors/')


# decorators


def get_all_decorators(request):
    decorators = Decorator.objects.all().values()
    employee = Employee.objects.filter(passport__in=decorators)
    template = loader.get_template('decorators-table.html')
    context = {
        'decorators': employee,
        'title': 'Decorators',
    }
    return HttpResponse(template.render(context, request))


def add_decorator(request):
    try:
        if request.method == "POST":
            form = DecoratorForm(request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                post.save()
                return redirect('/decorators/')
        else:
            form = DecoratorForm()
        context = {
            'form': form,
            'title': 'Decorators',
            'action': 'Add',
        }
        return render(request, 'add-edit.html', context=context)
    except():
        return HttpResponseRedirect('/decorators/')


def delete_decorator(request, participant_id):
    decorator = Decorator.objects.get(participant_id=participant_id)
    decorator.delete()
    return HttpResponseRedirect('/decorators/')


# playdirectors


def get_all_playdirectors(request):
    playdirectors = PlayDirector.objects.all().values()
    employee = Employee.objects.filter(passport__in=playdirectors)
    template = loader.get_template('playdirectors-table.html')
    context = {
        'playdirectors': employee,
        'title': 'Directors of plays',
    }
    return HttpResponse(template.render(context, request))


def add_playdirector(request):
    try:
        if request.method == "POST":
            form = PlayDirectorForm(request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                post.save()
                return redirect('/playdirectors/')
        else:
            form = PlayDirectorForm()
        context = {
            'form': form,
            'title': 'Directors of plays',
            'action': 'Add',
        }
        return render(request, 'add-edit.html', context=context)
    except():
        return HttpResponseRedirect('/playdirectors/')


def delete_playdirector(request, participant_id):
    playdirector = PlayDirector.objects.get(participant_id=participant_id)
    playdirector.delete()
    return HttpResponseRedirect('/playdirectors/')


# actors


def get_all_actors(request):
    actors = Actor.objects.all().values()
    employee = Employee.objects.filter(passport__in=actors)
    template = loader.get_template('actors-table.html')
    context = {
        'actors': employee,
        'title': 'Actors',
    }
    return HttpResponse(template.render(context, request))


def add_actor(request):
    try:
        if request.method == "POST":
            form = ActorForm(request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                post.save()
                return redirect('/actors/')
        else:
            form = ActorForm()
        context = {
            'form': form,
            'title': 'Actors',
            'action': 'Add',
        }
        return render(request, 'add-edit.html', context=context)
    except():
        return HttpResponseRedirect('/actors/')


def delete_actor(request, participant_id):
    actor = Actor.objects.get(participant_id=participant_id)
    actor.delete()
    return HttpResponseRedirect('/actors/')


# roles


def get_all_roles(request):
    roles = Role.objects.all()
    template = loader.get_template('roles-table.html')
    context = {
        'roles': roles,
        'title': 'Roles',
    }
    return HttpResponse(template.render(context, request))


def add_role(request):
    try:
        if request.method == "POST":
            form = RoleForm(request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                post.save()
                return redirect('/roles/')
        else:
            form = RoleForm()
        context = {
            'form': form,
            'title': 'Roles',
            'action': 'Add',
        }
        return render(request, 'add-edit.html', context=context)
    except():
        return HttpResponseRedirect('/roles/')


def edit_role(request, name):
    try:
        roles = get_object_or_404(Role, name=name)
        form = RoleForm(request.POST or None, instance=roles)
        if form.is_valid():
            if form['name'].value() != name:
                messages.error(request, 'You can not change name.')
                return redirect('edit-role', name)
            else:
                form.save()
                return redirect('list-roles')
        context = {
            'form': form,
            'title': 'Roles',
            'action': 'Edit',
        }
        return render(request, 'add-edit.html', context)
    except():
        return HttpResponseRedirect('/roles/')


def delete_role(request, name):
    role = Role.objects.get(name=name)
    role.delete()
    return HttpResponseRedirect('/roles/')


# put_on


def get_all_put_on(request):
    put_on = PutOn.objects.all()
    template = loader.get_template('put-on-table.html')
    context = {
        'put_on': put_on,
        'title': 'Put on',
    }
    return HttpResponse(template.render(context, request))


def add_put_on(request):
    try:
        if request.method == "POST":
            form = PutOnForm(request.POST)
            queryset = PutOn.objects.filter(participant_id=form['participant'].value())
            queryset = queryset.filter(theater_id=form['theater'].value())
            queryset = queryset.filter(performance_id=form['performance'].value())
            if queryset.count() != 0:
                messages.error(request, 'Participant has already put on performance in that theater.')
                return redirect('/put-on/add')
            if form.is_valid():
                post = form.save(commit=False)
                post.save()
                return redirect('/put-on/')
        else:
            form = PutOnForm()
        context = {
            'form': form,
            'title': 'Put on',
            'action': 'Add',
        }
        return render(request, 'add-edit.html', context=context)
    except():
        return HttpResponseRedirect('/put-on/')


def edit_put_on(request, id):
    try:
        put_on = get_object_or_404(PutOn, id=id)
        form = PutOnForm(request.POST or None, instance=put_on)
        if form.is_valid():
            queryset = PutOn.objects.filter(participant_id=form['participant'].value())
            queryset = queryset.filter(theater_id=form['theater'].value())
            queryset = queryset.filter(performance_id=form['performance'].value())
            if queryset.count() != 0:
                messages.error(request, 'Participant has already put on performance in that theater.')
                return redirect('/put-on/add')
            form.save()
            return redirect('list-put-on')
        else:
            context = {
                'form': form,
                'title': 'Put on',
                'action': 'Edit',
            }
            return render(request, 'add-edit.html', context)
    except():
        return HttpResponseRedirect('/put-on/')


def delete_put_on(request, id):
    put_on = PutOn.objects.get(id=id)
    put_on.delete()
    return HttpResponseRedirect('/put-on/')


# queries


def query_page(request):
    query_dict = request.GET
    participants_all = Participant.objects.all()
    theaters_all = Theater.objects.all()

    query1_N = query_dict.get('query1-N')
    query1 = Theater.objects.raw(
        """
         Select name
        From lab_theater
        Join lab_employee_theater on lab_employee_theater.theater_id = lab_theater.name
        Where (
            Select count(*)
            From lab_employee
            Where lab_employee.sex = 'female' and lab_employee_theater.employee_id = lab_employee.passport
        ) >= %s
        """,
        [query1_N])

    query2_A = query_dict.get('query2-A')
    query2 = Performance.objects.raw(
        """
        Select *
        From lab_performance
        Join lab_puton on lab_puton.performance_id = lab_performance.title
        Join lab_participant on lab_puton.participant_id = lab_participant.employee_id
        Where lab_participant.employee_id = %s;
        """,
        [query2_A])

    query3_A = query_dict.get('query3-A')
    print()
    query3 = Employee.objects.raw(
        """
        Select passport, name
        From lab_employee
        Where lab_employee.passport in (
            Select distinct lab_actor.participant_id
            From lab_actor
            Join lab_role on lab_role.actor_id = lab_actor.participant_id
            Join lab_performance on lab_performance.title = lab_role.performance_title_id
            Join lab_puton on lab_performance.title = lab_puton.performance_id
            Where lab_puton.theater_id = %s and lab_role.type = 'secondary'
        );
        """,
        [query3_A])

    query4_N = query_dict.get('query4-N')
    query4 = Theater.objects.raw(
        """
        Select lab_theater.name
        From lab_theater
        Join lab_director on lab_director.theater_id = lab_theater.name
        Join lab_employee on lab_employee.passport = lab_director.employee_id
        Where lab_employee.experience > %s;
        """,
        [query4_N])

    query4_N = query_dict.get('query4-N')
    query4 = Theater.objects.raw(
        """
        Select lab_theater.name
        From lab_theater
        Join lab_director on lab_director.theater_id = lab_theater.name
        Join lab_employee on lab_employee.passport = lab_director.employee_id
        Where lab_employee.experience > %s;
        """,
        [query4_N])

    query5_B = query_dict.get('query5-B')
    query5 = Theater.objects.raw(
        """
        Select lab_theater.name
        From lab_theater
        Join lab_director on lab_director.theater_id = lab_theater.name
        Join lab_employee on lab_employee.passport = lab_director.employee_id
        Where lab_employee.experience > %s;
        """,
        [query5_B])

    context = {
        'query1': query1,
        'query2': query2,
        'query3': query3,
        'query4': query4,
        'query5': query5,
        'participants': participants_all,
        'theaters': theaters_all,
    }
    return render(request, 'queries.html', context=context)

