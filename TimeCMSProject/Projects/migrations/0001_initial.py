# Generated by Django 4.1.2 on 2022-10-27 08:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Departments', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProgressStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.TextField(max_length=255)),
                ('deadline', models.DateTimeField(blank=True, null=True)),
                ('priority', models.CharField(choices=[('Highest', 'Highest'), ('Lowest', 'Lowest'), ('Medium', 'Medium')], default='Lowest', max_length=255)),
                ('is_ongoing', models.BooleanField(default=True)),
                ('is_completed', models.BooleanField(default=False)),
                ('received_at', models.DateTimeField(auto_now_add=True)),
                ('completed_at', models.DateTimeField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('department', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Departments.departments')),
                ('progress_status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Projects.progressstatus')),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=1000, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('priority', models.CharField(choices=[('Highest', 'Highest'), ('Lowest', 'Lowest'), ('Medium', 'Medium')], default='Lowest', max_length=255)),
                ('deadline', models.DateTimeField(blank=True, null=True)),
                ('task_created_by', models.CharField(blank=True, max_length=255, null=True)),
                ('is_completed', models.BooleanField(default=False)),
                ('started_at', models.DateTimeField(blank=True, null=True)),
                ('completed_at', models.DateTimeField(blank=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('assigned_to', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('department', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Departments.departments')),
                ('progress_status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Projects.progressstatus')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Projects.projects')),
            ],
        ),
        migrations.CreateModel(
            name='Remarks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Projects.projects')),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Projects.task')),
            ],
        ),
    ]
