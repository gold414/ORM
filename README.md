# Ex02 Django ORM Web Application
## Date: 13-09-2025

## AIM
To develop a Django application to store and retrieve data from a Car Inventory Database using Object Relational Mapping(ORM).

## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 10 books

## PROGRAM
```
models.py

from django.db import models
from django.contrib import admin
class Car_DB(models.Model):
           Car_brand = models.CharField(max_length = 15)
           Car_model = models.CharField(max_length = 10)
           Car_type  = models.CharField(max_length = 8)
           VIN_no    = models.CharField(max_length = 17,primary_key = True)
class DBAdmin(admin.ModelAdmin):
    list_display = ["Car_brand","Car_model","Car_type","VIN_no"]

admin.py

from django.contrib import admin
from .models import Car_DB, DBAdmin
admin.site.register(Car_DB,DBAdmin)

```


## OUTPUT
![alt text](<Screenshot (14).png>)


## RESULT
Thus the program for creating car inventory database database using ORM hass been executed successfully
