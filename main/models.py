from os import path

from django.db import models
from django.contrib.auth.models import User

from Light_Notebook.settings import BASE_DIR
from .model_support.mixins import NotesMixin


class Association(models.Model):
    title = models.CharField(max_length=1024, 
                             default='Default Association Name')
    description = models.CharField(max_length=1024,
                                   default='Default Association Description')
    chief = models.OneToOneField(User, on_delete=models.PROTECT)
    groups = models.ManyToManyField(to='Group')
    deals = models.ManyToManyField(to='Deal')
    tasks = models.ManyToManyField(to='Task')
    managers = models.ManyToManyField(to='Manager')
    customers = models.ManyToManyField(to='Customer')
    teams = models.ManyToManyField(to='Team')
    employees = models.ManyToManyField(to='Employee')    


class Deal(NotesMixin, models.Model):
    title = models.CharField(max_length=1024, default='Default Deal Title')
    description = models.CharField(max_length=2048, 
                                   default='Default Deal Description')
    deal_groups = models.ManyToManyField(to='Group')
    date_open = models.DateField(auto_now_add=True)
    deadline = models.DateField(null=True)
    date_done = models.DateField(null=True)
    is_closed = models.BooleanField(default=False)
    supervisors = models.ManyToManyField(to='Manager')
    customers = models.ManyToManyField(to='Customer')
    tasks = models.ManyToManyField(to='Task')
    budget = models.FloatField(default=0.0, null=True)
    expenses = models.FloatField(default=0.0, null=True)
    documents = models.ManyToManyField(to='Document')
    
    def add_expenses(self, amount:float) -> None:
        self.expenses += amount
        self.save()
    
    def get_balance(self) -> float | None:
        return self.budget - self.expenses


class Task(NotesMixin, models.Model):
    title = models.CharField(max_length=1024, default='Default Task Title')
    description = models.CharField(max_length=2048, 
                                   default='Default Task Description')    
    date_open = models.DateField(auto_now_add=True)
    deadline = models.DateField(null=True)
    date_done = models.DateField(null=True)
    managers = models.ManyToManyField(to='Manager')
    teams = models.ManyToManyField(to='Team')
    is_done = models.BooleanField(default=False)


class Manager(NotesMixin, models.Model):
    user = models.OneToOneField(to=User, on_delete=models.PROTECT)
    phone_number = models.CharField(max_length=64, default='+1234567890')
    profit = models.ManyToManyField(to='Profit')


class Customer(NotesMixin, models.Model):
    name = models.CharField(max_length=256, default='Default Customer Name')
    description = models.CharField(max_length=1024, 
                                   default='Default Customer Description')
    address = models.CharField(max_length=512, 
                               default='Default Customer Address')
    email = models.EmailField(max_length=64, 
                              default='default.customer@email.com')
    phone_number = models.CharField(max_length=16, default='+1234567890')
    employees = models.ManyToManyField(to='Employee')
    profit = models.ManyToManyField(to='Profit')


class Team(NotesMixin, models.Model):
    name = models.CharField(max_length=128, default='Default Team Name')
    description = models.CharField(max_length=256, 
                                   default='Default Team Description')
    managers = models.ManyToManyField(to='Manager')
    team_leader = models.OneToOneField(to='Employee', 
                                       on_delete=models.PROTECT, 
                                       related_name='foreman')
    employees = models.ManyToManyField(to='Employee')


class Employee(NotesMixin, models.Model):
    name = models.CharField(max_length=64, default='Default Employee Name')
    description = models.CharField(max_length=128, 
                                   default='Default Employee Description')
    phone_number = models.CharField(max_length=16, default='+1234567890')
    email = models.EmailField(max_length=64, 
                              default='default.employee@email.com')
    payment_status = models.CharField(max_length=128, 
                                      default='Payment Status Not Set')


class Note(models.Model):
    datetime_added = models.DateTimeField(auto_now_add=True)
    user = models.OneToOneField(to=User, on_delete=models.PROTECT)
    content = models.CharField(max_length=1024, default='Default Note Content')
    public = models.BooleanField(default=True)
    
     
class Document(models.Model):
    document = models.FileField(upload_to='documents/%Y/%m/%d')
    date_uploaded = models.DateField(auto_now_add=True)
    
    def get_document_path(self):
        return path.relpath(f'{BASE_DIR}/uploads/{self.document}')
    
    def get_display_name(self):
        last_slash = self.document.name.rfind('/')
        return self.document.name[last_slash + 1:]


class Profit(models.Model):
    date_earned = models.DateField(auto_now_add=True)
    amount = models.FloatField(default=0.0)


class Group(models.Model):
    name = models.CharField(max_length=256, default='Default Group Name')