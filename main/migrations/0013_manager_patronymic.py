# Generated by Django 4.1.5 on 2023-03-13 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_customer_notes_deal_notes_employee_notes_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='manager',
            name='patronymic',
            field=models.CharField(default=None, max_length=64, null=True),
        ),
    ]
