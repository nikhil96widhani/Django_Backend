# Generated by Django 2.1.7 on 2019-03-26 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('institutions', '0004_organization'),
    ]

    operations = [
        migrations.CreateModel(
            name='BaseOrganization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
            ],
            options={
                'db_table': 'base_organization',
                'managed': False,
            },
        ),
    ]
