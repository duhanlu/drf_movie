from django.db import models

TOP = [
    (False, 'No'),
    (True, 'Yes')
]
HOT = [
    (False, 'No'),
    (True, 'Yes')
]


SHOW = [
    (False, 'No'),
    (True, 'Yes')
]
FREE = [
    (False, 'No'),
    (True, 'Yes')
]
REGION = [
    (1, 'China mainland'),
    (2, 'China HongKong'),
    (3, 'United States'),
    (4, 'South Korean'),
    (5, 'Japan'),
    (6, 'Other')
]

QUALITY = [
    (1, '720P'),
    (2, '1080P'),
    (3, '4K')
]
# Create your models here.
class Category(models.Model):
    id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=100, verbose_name='Category')

    class Meta:
        db_table = u'category'
        verbose_name = 'category management'
        verbose_name_plural = 'category management'
    
    def __str__(self):
        return self.category_name

class Movie(models.Model):
    id = models.AutoField(primary_key=True)
    movie_name = models.CharField(max_length=100, verbose_name='movie name')
    release_year = models.IntegerField(verbose_name='release year')
    director = models.CharField(max_length=100, verbose_name='director')
    scriptwriter = models.CharField(max_length=200, verbose_name='script writer')
    actors = models.CharField(max_length=200, verbose_name='actor')
    region = models.SmallIntegerField(choices=REGION, verbose_name='region')
    types = models.CharField(max_length=200, verbose_name='types')
    language = models.CharField(max_length=200, verbose_name='language')
    release_date = models.DateField(verbose_name='release data')
    alternate_name = models.CharField(max_length = 100, blank=True, verbose_name='alternate name')
    duration = models.CharField(max_length=50, verbose_name='duration')
    image_url = models.CharField(max_length=200, verbose_name='image url')
    rate = models.FloatField(blank=True, verbose_name='rate')
    review = models.TextField(max_length=500, verbose_name='review')
    is_hot = models.BooleanField(choices=HOT, default=False, verbose_name='if hot')
    is_top = models.BooleanField(choices=TOP, default=False, verbose_name='if on the top')
    quality = models.SmallIntegerField(choices= QUALITY, blank=False, verbose_name='quality')
    subtitle = models.CharField(max_length=100, blank=True, verbose_name='subtitle')
    update_info = models.CharField(max_length=100, blank=True, verbose_name='update info')
    update_progress = models.CharField(max_length=100, blank=True, verbose_name='update progress')
    download_info = models.TextField(max_length=500, blank=True, verbose_name='download info')
    is_show = models.BooleanField(choices=SHOW, default=True, verbose_name='if showing')
    is_free = models.BooleanField(choices=FREE, default=False, verbose_name='if free')
    category = models.ForeignKey(Category, blank=False, verbose_name='category name', on_delete=models.CASCADE)

    class Meta:
        db_table = 'movie'
        verbose_name = 'movie management'
        verbose_name_plural = 'movie management'