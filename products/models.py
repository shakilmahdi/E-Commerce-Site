from django.db import models

# Create your models here.

class Product(models.Model):
    image = models.ImageField(upload_to='uploads/images', null= False, blank=False)
    name = models.CharField(max_length=150, null= False, blank=False)
    price = models.DecimalField(max_digits= 7, decimal_places=2, null= False, blank=False)
    description = models.TextField()
    category = models.CharField(max_length=50, null=True, blank=True)
    
    def __str__(self):
        return self.name

class User(models.Model):
    username = None
    email = models.EmailField(unique=True)
    
    USERNAME_FILED = 'email'
    REQUIREMENTS_FILED = []
    
    def __str__(self):
        return self.email