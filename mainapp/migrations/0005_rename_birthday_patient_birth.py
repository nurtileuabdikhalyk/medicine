# Generated by Django 4.1 on 2023-01-22 16:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0004_alter_doctor_user_alter_patient_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='patient',
            old_name='birthday',
            new_name='birth',
        ),
    ]