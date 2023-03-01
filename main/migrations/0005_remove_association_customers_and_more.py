# Generated by Django 4.1.5 on 2023-03-01 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_task_teams_alter_employee_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='association',
            name='customers',
        ),
        migrations.RemoveField(
            model_name='association',
            name='deals',
        ),
        migrations.RemoveField(
            model_name='association',
            name='employees',
        ),
        migrations.RemoveField(
            model_name='association',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='association',
            name='managers',
        ),
        migrations.RemoveField(
            model_name='association',
            name='tasks',
        ),
        migrations.RemoveField(
            model_name='association',
            name='teams',
        ),
        migrations.AddField(
            model_name='association',
            name='customers',
            field=models.ManyToManyField(to='main.customer'),
        ),
        migrations.AddField(
            model_name='association',
            name='deals',
            field=models.ManyToManyField(to='main.deal'),
        ),
        migrations.AddField(
            model_name='association',
            name='employees',
            field=models.ManyToManyField(to='main.employee'),
        ),
        migrations.AddField(
            model_name='association',
            name='groups',
            field=models.ManyToManyField(to='main.group'),
        ),
        migrations.AddField(
            model_name='association',
            name='managers',
            field=models.ManyToManyField(to='main.manager'),
        ),
        migrations.AddField(
            model_name='association',
            name='tasks',
            field=models.ManyToManyField(to='main.task'),
        ),
        migrations.AddField(
            model_name='association',
            name='teams',
            field=models.ManyToManyField(to='main.team'),
        ),
    ]
