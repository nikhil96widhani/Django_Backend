from django.db import models
from django.contrib.auth.models import User
from organization.models import Organization

class Profile(models.Model):
    ADMIN = 1
    STAFF = 2
    INSTITUTION_ADMIN = 3
    INSTITUTION_TTO = 4
    ROLE_CHOICES = (
        (ADMIN, 'Admin'),
        (STAFF, 'Staff'),
        (INSTITUTION_ADMIN, 'Institution Admin'),
        (INSTITUTION_TTO, 'Institution TTO'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    bio = models.TextField(max_length=500, blank=True)
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, null=True, blank=True)
    org_key = models.ForeignKey(Organization, default=1, on_delete=models.DO_NOTHING)


    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kawrgs):
        super().save(*args, **kawrgs)
