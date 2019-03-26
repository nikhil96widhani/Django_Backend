from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    bio = models.TextField(max_length=500, blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kawrgs):
        super().save(*args, **kawrgs)

class Organization(models.Model):
    name_en = models.TextField()
    name_fr = models.TextField()
    street_address = models.TextField()
    city = models.TextField()
    province = models.TextField()
    postal_code = models.TextField()
    country = models.TextField()
    website_url = models.TextField()
    main_telephone = models.TextField()
    logo_path = models.TextField()
    is_research_funder = models.BooleanField(max_length=100)
    is_research_org = models.BooleanField(max_length=100)
    is_business = models.BooleanField(max_length=100)
    is_non_profit = models.BooleanField(max_length=100)
    is_govt = models.BooleanField(max_length=100)

    class Meta:
        managed = False
        db_table = 'organization'