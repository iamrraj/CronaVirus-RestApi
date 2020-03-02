from django.db import models
from django.conf import settings
from datetime import datetime
from django.contrib.auth.models import User
from django.utils.timezone import now
import requests
# Create your models here.


class CronaVirus(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    currentConfirmedCount = models.IntegerField(
        blank=True, null=True, help_text="Number of current remaining confirmed patients ")
    confirmCount = models.IntegerField(
        blank=True, null=True, help_text="Number of confirmed patients ")
    suspectedCount = models.IntegerField(
        blank=True, null=True, help_text="Number of suspected patients ")
    curedCount = models.IntegerField(
        blank=True, null=True, help_text="Number of cured patients ")
    deadCount = models.IntegerField(
        blank=True, null=True, help_text="Number of dead patients ")
    seriousCount = models.IntegerField(
        blank=True, null=True, help_text="Number of serious patients ")
    currentConfirmedIncr = models.IntegerField(
        blank=True, null=True, help_text="Number of current remaining confirmed patients (increased from yesterday)")
    confirmIncr = models.IntegerField(
        blank=True, null=True, help_text="Number of confirmed patients (increased from yesterday)")
    suspectedIncr = models.IntegerField(
        blank=True, null=True, help_text="Number of suspected infection (increased from yesterday)")
    curedIncr = models.IntegerField(
        blank=True, null=True, help_text="Number of cured patients (increased from yesterday)")
    seriousIncr = models.IntegerField(
        blank=True, null=True, help_text="Number of critically ill (increased from yesterday)")
    deadIncr = models.IntegerField(
        blank=True, null=True, help_text="Number of death (increased from yesterday)")
    updateTime = models.BigIntegerField(
        blank=True, null=True, help_text="The latest updated time")
    note1 = models.CharField(max_length=255, blank=True,
                             null=True, help_text="Name of the virus")
    note2 = models.CharField(max_length=255, blank=True,
                             null=True, help_text="Source of infection")
    note3 = models.CharField(max_length=255, blank=True,
                             null=True, help_text="Way of spreading")

    def __str__(self):
        return self.note1


class Cities(models.Model):
    cityName = models.CharField(max_length=255, blank=True,
                                null=True, help_text="Name of the city ")
    locationId = models.BigIntegerField(
        blank=True, null=True, help_text="ID of cities In mainland China, the locationId is zip code, Outsides mainland China, the explanation of locationId is not sure ")
    currentConfirmedCount = models.BigIntegerField(
        blank=True, null=True, help_text="Number of current remaining confirmed patients ")
    confirmCount = models.BigIntegerField(
        blank=True, null=True, help_text="Number of confirmed patients ")
    suspectedCount = models.BigIntegerField(
        blank=True, null=True, help_text="Number of suspected patients ")
    curedCount = models.BigIntegerField(
        blank=True, null=True, help_text="Number of cured patients ")
    deadCount = models.BigIntegerField(
        blank=True, null=True, help_text="Number of dead patients ")

    def __str__(self):
        return self.cityName


class Area(models.Model):
    cities = models.ForeignKey(Cities, models.CASCADE, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updateTime = models.BigIntegerField(
        blank=True, null=True, help_text="The latest updated time")
    locationId = models.BigIntegerField(
        blank=True, null=True, help_text="ID of cities In mainland China, the locationId is zip code, Outsides mainland China, the explanation of locationId is not sure ")
    continentName = models.CharField(max_length=255, blank=True,
                                     null=True, help_text="Name of the continent ")
    country = models.CharField(max_length=255, blank=True,
                               null=True, help_text="Name of the country ")
    provinceName = models.CharField(max_length=255, blank=True,
                                    null=True, help_text="Name of the provinceName ")
    currentConfirmedCount = models.BigIntegerField(
        blank=True, null=True, help_text="Number of current remaining confirmed patients ")
    confirmCount = models.BigIntegerField(
        blank=True, null=True, help_text="Number of confirmed patients ")
    suspectedCount = models.BigIntegerField(
        blank=True, null=True, help_text="Number of suspected patients ")
    curedCount = models.BigIntegerField(
        blank=True, null=True, help_text="Number of cured patients ")
    deadCount = models.BigIntegerField(
        blank=True, null=True, help_text="Number of dead patients ")
    lat = models.FloatField(
        blank=True, null=True, help_text="Latitude of the country")
    lon = models.FloatField(
        blank=True, null=True, help_text="Longitude of the country")

    def __str__(self):
        return self.continentName


class News(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255, blank=True,
                             null=True, help_text="Title of the news")
    summary = models.TextField(blank=True, null=True)
    infosource = models.URLField(max_length=255, blank=True,
                                 null=True, help_text="Source Info")
    pubdate = models.BigIntegerField(
        blank=True, null=True, help_text="Publish date ")
    provinceName = models.CharField(max_length=255, blank=True,
                                    null=True, help_text="Proviance Name")
    provinceId = models.IntegerField(
        blank=True, null=True, help_text="ProvianceId ")

    def __str__(self):
        return self.title


class Remours(models.Model):

    timestamp = models.DateTimeField(auto_now_add=True)
    _id = models.IntegerField(
        blank=True, null=True, help_text="News Id ")
    title = models.CharField(max_length=255, blank=True,
                             null=True, help_text="Title of the news")
    mainSummary = models.CharField(max_length=255, blank=True,
                                   null=True, help_text="Main Summary of the news")
    body = models.TextField(blank=True, null=True, help_text="The reality")
    infosource = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.title
