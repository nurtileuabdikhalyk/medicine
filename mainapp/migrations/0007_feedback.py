# Generated by Django 4.1 on 2023-02-05 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0006_rename_birth_patient_birthday'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=150, verbose_name='Есімі')),
                ('last_name', models.CharField(max_length=150, verbose_name='Тегі')),
                ('message', models.TextField(verbose_name='Хабарлама мәтіні')),
            ],
            options={
                'verbose_name': 'Пікір',
                'verbose_name_plural': 'Пікірлер',
            },
        ),
    ]
