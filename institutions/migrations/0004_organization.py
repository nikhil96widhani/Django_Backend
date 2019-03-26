# Generated by Django 2.1.7 on 2019-03-22 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('institutions', '0003_profile_bio'),
    ]

    operations = [
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_en', models.TextField()),
                ('name_fr', models.TextField()),
                ('street_address', models.TextField()),
                ('city', models.TextField()),
                ('province', models.TextField()),
                ('postal_code', models.TextField()),
                ('country', models.TextField()),
                ('website_url', models.TextField()),
                ('main_telephone', models.TextField()),
                ('logo_path', models.TextField()),
                ('is_research_funder', models.BooleanField(max_length=100)),
                ('is_research_org', models.BooleanField(max_length=100)),
                ('is_business', models.BooleanField(max_length=100)),
                ('is_non_profit', models.BooleanField(max_length=100)),
                ('is_govt', models.BooleanField(max_length=100)),
            ],
            options={
                'db_table': 'organization',
                'managed': False,
            },
        ),
    ]
