from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.
class CharSheet(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    prof = models.CharField(max_length=12)
    attrs_str = models.IntegerField(default=10)
    attrs_dex = models.IntegerField(default=10)
    attrs_con = models.IntegerField(default=10)
    attrs_int = models.IntegerField(default=10)
    attrs_wis = models.IntegerField(default=10)
    attrs_cha = models.IntegerField(default=10)
    race = models.CharField(max_length=10)
    sex = models.CharField(max_length=10)
    alignment = models.CharField(max_length=10)

    name = models.CharField(max_length=12)
    background = models.TextField(max_length=300)
    bonds = models.TextField(max_length=300)
    ideals = models.TextField(max_length=300)
    flaws = models.TextField(max_length=300)

    avatar = models.ImageField(default='def_avatar.jpg', upload_to='avatars')

    def __str__(self):
        return f'{self.prof} created'

    def get_absolute_url(self):
        return reverse('journal')

    def save(self, *args, **kwargs):
        super(CharSheet, self).save(*args, **kwargs)

        img = Image.open(self.avatar.path)

        if img.height > 300 or img.width > 260:
            output_size = (300, 260)
            img.thumbnail(output_size)
            img.save(self.avatar.path)







