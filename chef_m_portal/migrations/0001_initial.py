# Generated by Django 5.0 on 2023-12-21 18:22

import django.core.validators
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
            name='Area',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=6, unique=True, validators=[django.core.validators.MinLengthValidator(6), django.core.validators.MaxLengthValidator(6)])),
                ('city', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='manager',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile', models.CharField(max_length=13, validators=[django.core.validators.MinLengthValidator(10), django.core.validators.MaxLengthValidator(13)])),
                ('wallet', models.IntegerField(default=0)),
                ('area', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='chef_m_portal.area')),
                ('chef_m', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='tables',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('table_name', models.CharField(max_length=20)),
                ('shape', models.CharField(max_length=10)),
                ('seats', models.CharField(max_length=2)),
                ('is_available', models.BooleanField(default=True)),
                ('size', models.CharField(max_length=100)),
                ('area', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='chef_m_portal.area')),
                ('people', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='chef_m_portal.manager')),
            ],
        ),
    ]
