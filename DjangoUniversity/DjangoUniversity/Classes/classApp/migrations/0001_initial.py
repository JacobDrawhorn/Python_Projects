# Generated by Django 3.2.7 on 2021-09-28 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='djangoClasses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=50)),
                ('Course_Number', models.IntegerField()),
                ('Instructor', models.CharField(max_length=50)),
                ('Duration', models.FloatField()),
            ],
        ),
    ]