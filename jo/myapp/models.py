from django.db import models
from django.contrib import admin
class mechanic_DB(models.Model):
    bike_No=models.CharField(max_length=20,primary_key=True)
    Name=models.CharField(max_length=10)
    mobile_no=models.IntegerField()
    owner_address=models.TextField()
    bike_name=models.CharField(max_length=10)
    date_of_bike_living=models.DateField()
    mechanic_no=models.CharField(max_length=20)
class mechanic_DBAdmin(admin.ModelAdmin):
    list_display=["bike_No","Name","mobile_no","owner_address","bike_name","date_of_bike_living","mechanic_no"]

