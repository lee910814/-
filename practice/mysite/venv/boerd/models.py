from django.db import models

# Create your models here.
class Input_Form(models.Model):
    subject = models.CharField(max_length=150)
    content = models.TextField()
    create_date = models.DateTimeField()