# Generated by Django 3.0.6 on 2020-05-30 23:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0021_auto_20200531_0611'),
    ]

    operations = [
        migrations.AlterField(
            model_name='follow',
            name='following',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='following_users', to=settings.AUTH_USER_MODEL, verbose_name='Автор постов'),
        ),
    ]
