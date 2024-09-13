from django.db import models

# Create your models here.
class Students(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    date_of_birth = models.DateField()

    def __str__(self) -> str:
        return f"{self.first_name}{self.last_name}"
    
