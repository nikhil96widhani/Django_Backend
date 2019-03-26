# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AlembicVersion(models.Model):
    version_num = models.CharField(primary_key=True, max_length=32)

    class Meta:
        managed = False
        db_table = 'alembic_version'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class BaseOrganization(models.Model):
    name = models.CharField(max_length=-1, blank=True, null=True)
    org = models.ForeignKey('Organization', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'base_organization'


class ContactInfo(models.Model):
    name = models.CharField(max_length=-1, blank=True, null=True)
    title = models.CharField(max_length=-1, blank=True, null=True)
    phone_number = models.CharField(max_length=-1, blank=True, null=True)
    email = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'contact_info'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Funding(models.Model):
    funder_tx_id = models.IntegerField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    amount = models.FloatField(blank=True, null=True)
    project = models.ForeignKey('Project', models.DO_NOTHING, blank=True, null=True)
    funding_program = models.ForeignKey('FundingPrograms', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'funding'


class FundingProgramTypes(models.Model):
    type = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'funding_program_types'


class FundingPrograms(models.Model):
    name = models.CharField(max_length=-1, blank=True, null=True)
    type = models.ForeignKey(FundingProgramTypes, models.DO_NOTHING, blank=True, null=True)
    funder = models.ForeignKey(BaseOrganization, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'funding_programs'


class InstitutionsProfile(models.Model):
    image = models.CharField(max_length=100)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING, unique=True)
    bio = models.TextField()

    class Meta:
        managed = False
        db_table = 'institutions_profile'


class Keyword(models.Model):
    id = models.BigAutoField(primary_key=True)
    en = models.CharField(max_length=-1, blank=True, null=True)
    fr = models.CharField(max_length=-1, blank=True, null=True)
    uk = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'keyword'


class KeywordAssociation(models.Model):
    project = models.ForeignKey('Project', models.DO_NOTHING, blank=True, null=True)
    keyword = models.ForeignKey(Keyword, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'keyword_association'


class Organization(models.Model):
    name_en = models.CharField(max_length=-1, blank=True, null=True)
    name_fr = models.CharField(max_length=-1, blank=True, null=True)
    street_address = models.CharField(max_length=-1, blank=True, null=True)
    city = models.CharField(max_length=-1, blank=True, null=True)
    province = models.CharField(max_length=-1, blank=True, null=True)
    postal_code = models.CharField(max_length=-1, blank=True, null=True)
    country = models.CharField(max_length=-1, blank=True, null=True)
    website_url = models.CharField(max_length=-1, blank=True, null=True)
    main_telephone = models.CharField(max_length=-1, blank=True, null=True)
    logo_path = models.CharField(max_length=-1, blank=True, null=True)
    ilo_contact = models.ForeignKey(ContactInfo, models.DO_NOTHING, blank=True, null=True)
    tto_contact = models.ForeignKey(ContactInfo, models.DO_NOTHING, blank=True, null=True)
    media_contact = models.ForeignKey(ContactInfo, models.DO_NOTHING, blank=True, null=True)
    is_research_funder = models.BooleanField(blank=True, null=True)
    is_research_org = models.BooleanField(blank=True, null=True)
    is_business = models.BooleanField(blank=True, null=True)
    is_non_profit = models.BooleanField(blank=True, null=True)
    is_govt = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'organization'


class PartnersAssociation(models.Model):
    project = models.ForeignKey('Project', models.DO_NOTHING, blank=True, null=True)
    base_organization = models.ForeignKey(BaseOrganization, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'partners_association'


# class PatentApplicant(models.Model):
#     original_name = models.CharField(max_length=-1, blank=True, null=True)
#     epo_name = models.CharField(max_length=-1, blank=True, null=True)
#     org = models.ForeignKey(BaseOrganization, models.DO_NOTHING, blank=True, null=True)
#     patent = models.ForeignKey('PatentPublication', models.DO_NOTHING, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'patent_applicant'


# class PatentCitationOther(models.Model):
#     patent = models.ForeignKey('PatentPublication', models.DO_NOTHING, blank=True, null=True)
#     citation_text = models.CharField(max_length=-1, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'patent_citation_other'


class PatentCitationPt(models.Model):
    patent = models.ForeignKey('PatentPublication', models.DO_NOTHING, blank=True, null=True)
    country = models.CharField(max_length=2, blank=True, null=True)
    doc_number = models.CharField(max_length=-1, blank=True, null=True)
    kind_code = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'patent_citation_pt'


class PatentFamily(models.Model):
    id = models.CharField(primary_key=True, max_length=-1)
    date_backfilled = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'patent_family'


class PatentInventor(models.Model):
    original_name = models.CharField(max_length=-1, blank=True, null=True)
    epo_name = models.CharField(max_length=-1, blank=True, null=True)
    given_name = models.CharField(max_length=-1, blank=True, null=True)
    family_name = models.CharField(max_length=-1, blank=True, null=True)
    initial = models.CharField(max_length=-1, blank=True, null=True)
    patent = models.ForeignKey('PatentPublication', models.DO_NOTHING, blank=True, null=True)
    person = models.ForeignKey('Person', models.DO_NOTHING, blank=True, null=True)
    affiliation = models.ForeignKey(BaseOrganization, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'patent_inventor'


class PatentPublication(models.Model):
    family = models.CharField(max_length=-1, blank=True, null=True)
    publication_epodoc = models.CharField(max_length=16, blank=True, null=True)
    publication_date = models.DateField(blank=True, null=True)
    application_epodoc = models.CharField(max_length=16, blank=True, null=True)
    application_date = models.DateField(blank=True, null=True)
    exemplar = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'patent_publication'


class PatentPublicationText(models.Model):
    patent = models.ForeignKey(PatentPublication, models.DO_NOTHING, blank=True, null=True)
    language = models.CharField(max_length=2, blank=True, null=True)
    title = models.CharField(max_length=-1, blank=True, null=True)
    abstract = models.CharField(max_length=-1, blank=True, null=True)
    description = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'patent_publication_text'


class Person(models.Model):
    family_name = models.CharField(max_length=-1, blank=True, null=True)
    given_name = models.CharField(max_length=-1, blank=True, null=True)
    initial = models.CharField(max_length=-1, blank=True, null=True)
    raw_name = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'person'


class Project(models.Model):
    id = models.CharField(primary_key=True, max_length=-1)
    title = models.CharField(max_length=-1, blank=True, null=True)
    summary = models.CharField(max_length=-1, blank=True, null=True)
    lead_org = models.ForeignKey(BaseOrganization, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'project'


class ProjectTeamMember(models.Model):
    project = models.ForeignKey(Project, models.DO_NOTHING, blank=True, null=True)
    person = models.ForeignKey(Person, models.DO_NOTHING, blank=True, null=True)
    affiliated_org = models.ForeignKey(BaseOrganization, models.DO_NOTHING, blank=True, null=True)
    family_name = models.CharField(max_length=-1, blank=True, null=True)
    given_name = models.CharField(max_length=-1, blank=True, null=True)
    initial = models.CharField(max_length=-1, blank=True, null=True)
    raw_name = models.CharField(max_length=-1, blank=True, null=True)
    role = models.CharField(max_length=5, blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'project_team_member'


class U15Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    time = models.DateTimeField()
    author = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'u15_post'
