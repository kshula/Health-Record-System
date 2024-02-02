# Generated by Django 5.0.1 on 2024-02-02 14:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('insurance_app', '0001_initial'),
        ('patient_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Nurse',
            fields=[
                ('auto_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('date_of_birth', models.DateField()),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('nrc', models.CharField(max_length=100)),
                ('address', models.TextField()),
                ('medical_number', models.PositiveIntegerField()),
                ('specialization', models.CharField(max_length=255)),
                ('years_of_experience', models.PositiveIntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=15)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('countries', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='insurance_app.country')),
                ('hospitals', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patient_app.medicalinformation')),
                ('provinces', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='insurance_app.province')),
                ('towns', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='insurance_app.town')),
            ],
        ),
    ]