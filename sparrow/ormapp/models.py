from django.db import models
from django.contrib import admin
class Car_DB(models.Model):
           Car_brand = models.CharField(max_length = 15)
           Car_model = models.CharField(max_length = 10)
           Car_type  = models.CharField(max_length = 8)
           VIN_no    = models.CharField(max_length = 17,primary_key = True)
class DBAdmin(admin.ModelAdmin):
    list_display = ["Car_brand","Car_model","Car_type","VIN_no"]
