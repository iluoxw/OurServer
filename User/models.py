# coding = utf-8
from django.db import models


class User(models.Model):
    username = models.CharField(max_length=32)
    name = models.CharField(max_length=32)
    password = models.CharField(max_length=32)
    delete_flag = models.CharField(max_length=4)


class Group(models.Model):
    group_name = models.CharField(max_length=32)
    delete_flag = models.CharField(max_length=4)


class Privileges(models.Model):
    pri_name = models.CharField(max_length=32)
    description = models.TextField()
    delete_flag = models.CharField(max_length=4)


class UserGroup(models.Model):
    userId = models.IntegerField()
    groupId = models.IntegerField()
    delete_flag = models.CharField(max_length=4)


class UserPrivileges(models.Model):
    userId = models.IntegerField()
    privilegesId = models.IntegerField()

    delete_flag = models.CharField(max_length=4)


class GroupPrivileges(models.Model):
    groupId = models.IntegerField()
    privilegesId = models.IntegerField()

    delete_flag = models.CharField(max_length=4)




# Create your models here.
