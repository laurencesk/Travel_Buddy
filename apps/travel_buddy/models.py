# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from datetime import date

class UserManager(models.Manager):
    def login_validator(self, postData):
        errors = {}
        if len(postData['name']) < 3:
            errors["name"] = "Name should be at least 3 characters"
        if len(postData['username']) < 3:
            errors["username"] = "Username should be at least 3 characters"        
        if len(postData['password']) < 8:
            errors["password"] = "Password should be at least 8 characters"
        if postData['password'] != postData['confirmpassword']:
            errors["password"] = "Your password do not match"
        return errors

class TripManager(models.Manager):
    def Trip_validator(self, postData):
        errors = {}
        if len(postData['destination']) < 1:
            errors["destination"] = "Destination cannot be empty" 
        if len(postData['description']) < 1:
            errors["description"] = "Description cannot be empty"     
        if postData['trave_end_date'] < postData['trave_start_date']:
            errors["trave_end_date"] = "Travel end date cannot be earlier than travel start date"
        if str(date.today()) > str(postData['trave_start_date']):
            errors["trave_start_date"] = "Trip start date cannot be in the past"
        if str(date.today()) > str(postData['trave_end_date']):
            errors["trave_end_date"] = "Trip end date cannot be in the past"
        return errors

class User(models.Model):
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()

class Trip(models.Model):
    destination = models.CharField(max_length=255)
    description = models.TextField()
    trave_start_date = models.DateField()
    trave_end_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    planned_by = models.ForeignKey(User, related_name = "plans")
    joined_by = models.ManyToManyField(User, related_name = "joins")
    objects = TripManager()
