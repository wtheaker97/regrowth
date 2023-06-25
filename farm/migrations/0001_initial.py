# Generated by Django 4.2.2 on 2023-06-25 12:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Farm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Created at')),
                ('modified_at', models.DateTimeField(auto_now=True, help_text='Modified at', null=True)),
                ('name', models.CharField(help_text='Farm name', max_length=255)),
                ('farm_type', models.CharField(choices=[('self_farmed', 'Self farmed'), ('tenented', 'Tenented')], default='self_farmed', max_length=32)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Farmer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Created at')),
                ('modified_at', models.DateTimeField(auto_now=True, help_text='Modified at', null=True)),
                ('first_name', models.CharField(help_text="Farmer's first name", max_length=255)),
                ('surname', models.CharField(help_text="Farmer's surname", max_length=255)),
                ('user', models.ForeignKey(blank=True, help_text='User account', null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Field',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Created at')),
                ('modified_at', models.DateTimeField(auto_now=True, help_text='Modified at', null=True)),
                ('name', models.CharField(help_text='Field name', max_length=255)),
                ('size', models.FloatField(help_text='Size of field (acres)')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='FarmFieldLinker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Created at')),
                ('modified_at', models.DateTimeField(auto_now=True, help_text='Modified at', null=True)),
                ('acquired_on', models.DateField(blank=True, help_text='Date the field was made part of the farm')),
                ('removed_on', models.DateField(blank=True, help_text='Date the field was removed from the farm')),
                ('farm', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='farm.farm')),
                ('field', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='farm.field')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='FarmFarmerLinker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Created at')),
                ('modified_at', models.DateTimeField(auto_now=True, help_text='Modified at', null=True)),
                ('started_on', models.DateField(help_text='Date the farmer started farming this farm')),
                ('stopped_on', models.DateField(help_text='Date the farmer stopped farming this farm')),
                ('farm', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='farm.farm')),
                ('farmer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='farm.farmer')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
