# Generated by Django 2.2 on 2020-03-01 14:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cities',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cityName', models.CharField(blank=True, help_text='Name of the city ', max_length=255, null=True)),
                ('locationId', models.IntegerField(blank=True, help_text='ID of cities In mainland China, the locationId is zip code, Outsides mainland China, the explanation of locationId is not sure ', null=True)),
                ('currentConfirmedCount', models.IntegerField(blank=True, help_text='Number of current remaining confirmed patients ', null=True)),
                ('confirmCount', models.IntegerField(blank=True, help_text='Number of confirmed patients ', null=True)),
                ('suspectedCount', models.IntegerField(blank=True, help_text='Number of suspected patients ', null=True)),
                ('curedCount', models.IntegerField(blank=True, help_text='Number of cured patients ', null=True)),
                ('deadCount', models.IntegerField(blank=True, help_text='Number of dead patients ', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CronaVirus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('currentConfirmedCount', models.IntegerField(blank=True, help_text='Number of current remaining confirmed patients ', null=True)),
                ('confirmCount', models.IntegerField(blank=True, help_text='Number of confirmed patients ', null=True)),
                ('suspectedCount', models.IntegerField(blank=True, help_text='Number of suspected patients ', null=True)),
                ('curedCount', models.IntegerField(blank=True, help_text='Number of cured patients ', null=True)),
                ('deadCount', models.IntegerField(blank=True, help_text='Number of dead patients ', null=True)),
                ('seriousCount', models.IntegerField(blank=True, help_text='Number of serious patients ', null=True)),
                ('currentConfirmedIncr', models.IntegerField(blank=True, help_text='Number of current remaining confirmed patients (increased from yesterday)', null=True)),
                ('confirmIncr', models.IntegerField(blank=True, help_text='Number of confirmed patients (increased from yesterday)', null=True)),
                ('suspectedIncr', models.IntegerField(blank=True, help_text='Number of suspected infection (increased from yesterday)', null=True)),
                ('curedIncr', models.IntegerField(blank=True, help_text='Number of cured patients (increased from yesterday)', null=True)),
                ('seriousIncr', models.IntegerField(blank=True, help_text='Number of critically ill (increased from yesterday)', null=True)),
                ('deadIncr', models.IntegerField(blank=True, help_text='Number of death (increased from yesterday)', null=True)),
                ('updateTime', models.IntegerField(blank=True, help_text='The latest updated time', null=True)),
                ('note1', models.CharField(blank=True, help_text='Name of the virus', max_length=255, null=True)),
                ('note2', models.CharField(blank=True, help_text='Source of infection', max_length=255, null=True)),
                ('note3', models.CharField(blank=True, help_text='Way of spreading', max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updateTime', models.IntegerField(blank=True, help_text='The latest updated time', null=True)),
                ('locationId', models.IntegerField(blank=True, help_text='ID of cities In mainland China, the locationId is zip code, Outsides mainland China, the explanation of locationId is not sure ', null=True)),
                ('continentName', models.CharField(blank=True, help_text='Name of the continent ', max_length=255, null=True)),
                ('country', models.CharField(blank=True, help_text='Name of the country ', max_length=255, null=True)),
                ('provinceName', models.CharField(blank=True, help_text='Name of the provinceName ', max_length=255, null=True)),
                ('currentConfirmedCount', models.IntegerField(blank=True, help_text='Number of current remaining confirmed patients ', null=True)),
                ('confirmCount', models.IntegerField(blank=True, help_text='Number of confirmed patients ', null=True)),
                ('suspectedCount', models.IntegerField(blank=True, help_text='Number of suspected patients ', null=True)),
                ('curedCount', models.IntegerField(blank=True, help_text='Number of cured patients ', null=True)),
                ('deadCount', models.IntegerField(blank=True, help_text='Number of dead patients ', null=True)),
                ('lat', models.FloatField(blank=True, help_text='Latitude of the country', null=True)),
                ('lon', models.FloatField(blank=True, help_text='Longitude of the country', null=True)),
                ('cities', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CronaVirus.Cities')),
            ],
        ),
    ]
