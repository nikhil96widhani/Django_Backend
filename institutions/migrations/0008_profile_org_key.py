# Generated by Django 2.1.7 on 2019-04-12 17:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0001_initial'),
        ('institutions', '0007_profile_role'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='org_key',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='organization.Organization'),
        ),
    ]
