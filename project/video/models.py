from django.core.validators import FileExtensionValidator
from django.db import models

# Create your models here.



class Video(models.Model):
    '''Video yuklash uchun model'''
    video = models.FileField(upload_to='videos/', validators=[
        FileExtensionValidator(allowed_extensions=['mp4', 'WMW'])
    ])



class Image(models.Model):
    '''Rasm yuklash uchun model'''
    image = models.ImageField(upload_to='image/')