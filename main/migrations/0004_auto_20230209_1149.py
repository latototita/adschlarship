# Generated by Django 3.2 on 2023-02-09 11:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20230105_1026'),
    ]

    operations = [
        migrations.RenameField(
            model_name='form2',
            old_name='file',
            new_name='Cv',
        ),
        migrations.RenameField(
            model_name='form2',
            old_name='letter_to_manager',
            new_name='letter_to_employer',
        ),
        migrations.RemoveField(
            model_name='form2',
            name='Family_total_income_level',
        ),
        migrations.RemoveField(
            model_name='form2',
            name='number_of_children_in_the_family',
        ),
        migrations.RemoveField(
            model_name='form2',
            name='number_of_family_members',
        ),
    ]
