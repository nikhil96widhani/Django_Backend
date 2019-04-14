from django.db import models
from django.contrib.auth.models import User


class ContactInfo(models.Model):
    name = models.TextField()
    title = models.TextField()
    phone_number = models.TextField()
    email = models.TextField()

    class Meta:
        managed = False
        db_table = 'contact_info'


class Organization(models.Model):
    id = models.IntegerField(primary_key=True)
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
    # ilo_contact = models.ForeignKey(ContactInfo, models.DO_NOTHING, related_name='ilo_contact_set')
    # tto_contact = models.ForeignKey(ContactInfo, models.DO_NOTHING,  related_name='tto_contact_set')
    # media_contact = models.ForeignKey(ContactInfo, models.DO_NOTHING, related_name='media_contact_set')
    is_research_funder = models.BooleanField(max_length=100)
    is_research_org = models.BooleanField(max_length=100)
    is_business = models.BooleanField(max_length=100)
    is_non_profit = models.BooleanField(max_length=100)
    is_govt = models.BooleanField(max_length=100)
    #usermap = models.ForeignKey(User, on_delete=models.PROTECT, default=1)

    class Meta:
        managed = False
        db_table = 'organization'

    def __str__(self):
        return self.name_en


class BaseOrganization(models.Model):
    name = models.TextField()
    org = models.ForeignKey('Organization', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'base_organization'
