# Generated by Django 3.0.6 on 2020-05-29 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_remove_group_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='title',
            field=models.CharField(default=None, max_length=200, null=True),
        ),
    ]
