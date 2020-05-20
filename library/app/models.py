from django.db import models

# Create your models here.

class BookModel(models.Model):
    title=models.CharField(max_length=100)
    author_name=models.CharField(max_length=150)
    description=models.TextField(blank=True)
    image=models.ImageField(blank=True)
    issue_state=models.BooleanField(default=False)


    def __str__(self):
        return self.title
