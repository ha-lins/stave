from django.db import models

class Project(models.Model):
    pro_name = models.CharField(max_length=200)
    ontology = models.TextField(default='')


class Document(models.Model):
    name = models.CharField(max_length=200)
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        default=''
    )
    textPack = models.TextField()


class User(models.Model):
    name = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
