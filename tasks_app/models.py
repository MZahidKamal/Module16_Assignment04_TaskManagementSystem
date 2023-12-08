from django.db import models
from categories_app.models import Categories_Model

# Create your models here.
class Tasks_Model(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    assign_date = models.DateTimeField(unique=True)
    category = models.ManyToManyField(Categories_Model, null=False)

    def __str__(self):
        return self.title
