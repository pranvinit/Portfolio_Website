# Generated by Django 3.2.9 on 2022-03-18 04:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20220318_0905'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('detail', models.TextField(blank=True, null=True)),
                ('images', models.CharField(blank=True, max_length=255, null=True)),
                ('video', models.CharField(blank=True, max_length=100, null=True)),
                ('github', models.CharField(max_length=100)),
                ('hosted_on', models.CharField(blank=True, max_length=100, null=True)),
                ('infrastructure', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]