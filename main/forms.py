from django import forms

from .models import (
    Deal,
    Task,
    Team,
    Group,
    Employee,
    Customer,
)


class DealForm(forms.ModelForm):
    class Meta():
        model = Deal
        fields = [
            'title',
            'description',
            'deal_groups',
            'deadline',
            'supervisors',
            'customers',
            'tasks',
            'budget',
            'documents',
        ]
        labels = {
            'title': 'Название сделки',
            'description': 'Описание сделки',
            'deal_groups': 'Группы сделок',
            'deadline': 'Дата окончания сделки',
            'supervisors': 'Ответственные',
            'customers': 'Клиенты (Заказчики)',
            'tasks': 'Задачи',
            'budget': 'Бюджет',
            'documents': 'Документы (Файлы)'
        }
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-text',
                'placeholder': 'Название сделки',
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-text',
                'cols': 60,
                'rows': 15,
                'placeholder': 'Описание сделки',
            }),
            'deadline': forms.DateInput(attrs={
                'placeholder': 'ГГГГ-ММ-ДД',
            }),
            'documents': forms.FileInput(),
        }


class TaskForm(forms.ModelForm):
    class Meta():
        model = Task
        fields = [
            'title',
            'description',
            'deadline',
            'managers',
            'teams',
        ]
        labels = {
            'title': 'Название задачи',
            'description': 'Описание задачи',
            'deadline': 'Срок выполнения задачи',
            'managers': 'Руководители задачи',
            'teams': 'Рабочие команды',
        }
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-text',
                'placeholder': 'Название задачи',
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-text',
                'cols': 60,
                'rows': 15,
                'placeholder': 'Описание задачи',
            }),
            'deadline': forms.DateInput(attrs={
                'placeholder': 'ГГГГ-ММ-ДД',
            }),
        }      


class TeamForm(forms.ModelForm):
    class Meta():
        model = Team
        fields = [
            'name',
            'description',
            'managers',
            'team_leader',
            'employees',
        ]
        labels = {
            'name': 'Название команды',
            'description': 'Описание команды',
            'managers': 'Менеджеры команды',
            'team_leader': 'Лидер команды',
            'employees': 'Участники команды',
        }
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-text',
                'placeholder': 'Название команды',
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-text',
                'cols': 60,
                'rows': 15,
                'placeholder': 'Описание команды',
            }),
        }


class EmployeeForm(forms.ModelForm):
    class Meta():
        model = Employee
        fields = [
            'name',
            'description',
            'phone_number',
            'email',
            'payment_status',
        ]
        labels = {
            'name': 'Имя работника',
            'description': 'Сводка о работнике',
            'phone_number': 'Номер телефона',
            'email': 'Эл. почта',
            'payment_status': 'Статус оплаты',
        }
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-text',
                'placeholder': 'Имя работника',
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-text',
                'cols': 60,
                'rows': 15,
                'placeholder': 'Сводка о работнике',
            }),
        }


class CustomerForm(forms.ModelForm):
    class Meta():
        model = Customer
        fields = [
            'name',
            'description',
            'address',
            'email',
            'phone_number',
            'employees',
        ]
        labels = {
            'name': 'Имя клиента',
            'description': 'Сводка о клиенте',
            'address': 'Адрес клиенте',
            'email': 'Эл. почта',
            'phone_number': 'Номер телефона',
            'employees': 'Сотрудники клиента',
        }
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-text',
                'placeholder': 'Имя клиента',
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-text',
                'cols': 60,
                'rows': 15,
                'placeholder': 'Сводка о клиенте',
            }),
        }


class GroupForm(forms.ModelForm):
    class Meta():
        model = Group
        fields = ['name']
        labels = {'name': 'Название группы'}
        widgets = {'name': forms.TextInput(attrs={
            'class': 'form-text',
            'placeholder': 'Название группы',
        })}