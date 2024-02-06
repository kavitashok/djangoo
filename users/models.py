from django.db import models
from django.contrib.auth.models import User
from PIL import Image
import os
from datetime import datetime

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg',upload_to='profile_pics')

def __str__(self):
   return f'{self.user.username} Profile'

def save(self, *args, **kawrgs):
    super().save(*args, **kawrgs)

    img = Image.open(self.image.path)

    if img.height > 300 or img.width > 300:
        output_size = (300, 300)
        img.thumbnail(output_size)
        #resized_width, resized_height = img.size
        #print(f"Resized Image Size: {resized_width} x {resized_height} pixels")
        img.save(self.image.path,format='JPEG', quality=95)
