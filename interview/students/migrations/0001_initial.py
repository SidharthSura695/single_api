# Generated by Django 3.1.3 on 2025-03-28 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudentMarks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_id', models.IntegerField(unique=True)),
                ('marks', models.IntegerField()),
            ],
        ),
    ]
