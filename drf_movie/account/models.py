from django.db import models
from django.contrib.auth.models import User
from shortuuidfield import ShortUUIDField

from movie.models import Movie

# Create your models here.
class Profile(models.Model):
    
    uid = ShortUUIDField(max_length=32, primary_key=True, unique=True, verbose_name='unique id')
    phone = models.CharField(max_length=11, blank=True, null=True, verbose_name='user phone number', db_index=True)
    email = models.CharField(max_length=40, blank=True, null=True, verbose_name='user email', db_index=True)
    avatar = models.CharField(max_length=60, blank=True, null=True, verbose_name='user avatar')
    
    is_upgrade = models.IntegerField(default = 0, verbose_name='if upgrade')
    upgrade_time = models.DateTimeField(blank=True, null=True, verbose_name='upgrade date')
    expire_time = models.DateTimeField(blank=True, null=True, verbose_name='expire date')
    upgrade_count = models.IntegerField(default=0, verbose_name='upgrade count')
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    movies = models.ManyToManyField(Movie)
    
    class Meta: 
        db_table='profile'
        verbose_name = 'user info'
        verbose_name_plural = 'user info'