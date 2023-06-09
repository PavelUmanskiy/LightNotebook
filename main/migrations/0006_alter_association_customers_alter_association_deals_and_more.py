# Generated by Django 4.1.5 on 2023-03-01 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_remove_association_customers_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='association',
            name='customers',
            field=models.ManyToManyField(null=True, to='main.customer'),
        ),
        migrations.AlterField(
            model_name='association',
            name='deals',
            field=models.ManyToManyField(null=True, to='main.deal'),
        ),
        migrations.AlterField(
            model_name='association',
            name='employees',
            field=models.ManyToManyField(null=True, to='main.employee'),
        ),
        migrations.AlterField(
            model_name='association',
            name='groups',
            field=models.ManyToManyField(null=True, to='main.group'),
        ),
        migrations.AlterField(
            model_name='association',
            name='managers',
            field=models.ManyToManyField(null=True, to='main.manager'),
        ),
        migrations.AlterField(
            model_name='association',
            name='tasks',
            field=models.ManyToManyField(null=True, to='main.task'),
        ),
        migrations.AlterField(
            model_name='association',
            name='teams',
            field=models.ManyToManyField(null=True, to='main.team'),
        ),
    ]
