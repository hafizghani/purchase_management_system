"""
Definition of models.
"""

from django.db import models
from decimal import Decimal
from django.contrib.auth.models import User

#sharing entity

class UserInfo(models.Model):
    user_id = models.OneToOneField(User)
    user_address = models.TextField()
    user_phone_number = models.TextField()
    user_role = models.TextField()
    def __chr__(self):
        return str(self.user_id)

class Vendor(models.Model):
    vendor_id = models.CharField(primary_key=True, max_length=10)
    vendor_name = models.TextField()
    vendor_phone_number = models.TextField()
    vendor_address = models.TextField()
    vendor_email = models.TextField()
    def __str__(self):
        return str(self.vendor_id)

class Item(models.Model):
    item_id = models.CharField(primary_key=True, max_length=10)
    item_name = models.TextField()
    item_description = models.TextField(null=True,default=None, blank=True)
    def __str__(self):
        return str(self.item_id)
