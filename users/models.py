from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    image = CloudinaryField('image', blank=True, null=True)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    
    def __str__(self):
        return self.name
    # @property
    # def username(self):
    #     return self.user.username
    
    # def __str__(self):
    #     return f'{self.user.username} Customer'
    
    # @receiver(post_save, sender=User)
    # def create_customer(sender, instance, created, **kwargs):
    #     if created:
    #         Customer.objects.create(user=instance)
            

    # @receiver(post_save, sender=User)
    # def save_customer(sender, instance, **kwargs):
    #     instance.customer.save()