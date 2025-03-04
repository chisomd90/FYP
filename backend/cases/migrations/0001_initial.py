# Generated by Django 5.1.2 on 2025-01-24 19:28

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Case',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('case_number', models.CharField(max_length=255, unique=True)),
                ('title', models.CharField(max_length=255)),
                ('plaintiff', models.CharField(max_length=255)),
                ('defendant', models.CharField(max_length=255)),
                ('status', models.CharField(choices=[('ongoing', 'Ongoing'), ('closed', 'Closed')], max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='created_cases', to=settings.AUTH_USER_MODEL)),
                ('judge', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='judged_cases', to=settings.AUTH_USER_MODEL)),
                ('lawyer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='lawyer_cases', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
