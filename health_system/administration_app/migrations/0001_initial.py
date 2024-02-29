# Generated by Django 5.0.1 on 2024-02-22 19:48

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('countries', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Administrator',
            fields=[
                ('auto_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('date_of_birth', models.DateField()),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('nrc', models.CharField(max_length=255)),
                ('address', models.TextField()),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=15)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.group')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('countries', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administration_app.country')),
            ],
        ),
        migrations.CreateModel(
            name='AdministratorImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='Images/Medical_Stuff_Images/Administrator_Images/')),
                ('description', models.TextField(blank=True, null=True)),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('administrator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administration_app.administrator')),
            ],
        ),
        migrations.CreateModel(
            name='Province',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('provinces', models.CharField(max_length=100)),
                ('countries', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administration_app.country')),
            ],
        ),
        migrations.AddField(
            model_name='administrator',
            name='provinces',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administration_app.province'),
        ),
        migrations.CreateModel(
            name='Town',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('towns', models.CharField(max_length=100)),
                ('countries', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administration_app.country')),
                ('provinces', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administration_app.province')),
            ],
        ),
        migrations.AddField(
            model_name='administrator',
            name='towns',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administration_app.town'),
        ),
    ]
