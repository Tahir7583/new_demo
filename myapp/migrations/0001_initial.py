# Generated by Django 5.0.3 on 2024-09-11 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recruiters',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(max_length=100)),
                ('dob', models.DateField()),
                ('phone', models.IntegerField()),
                ('marital_status', models.CharField(max_length=100)),
                ('home_town', models.CharField(max_length=100)),
                ('pincode', models.IntegerField()),
                ('curent_location', models.CharField(max_length=100)),
                ('experince', models.IntegerField()),
                ('language', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Recruiter_Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('degree', models.CharField(max_length=100)),
                ('fields_of_specialization', models.CharField(max_length=100)),
                ('institute_name', models.CharField(max_length=200)),
                ('data_of_completion', models.DateField()),
                ('recruiter_id', models.ManyToManyField(related_name='recruiter_id', to='myapp.recruiters')),
            ],
        ),
    ]