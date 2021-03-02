# Generated by Django 3.1.5 on 2021-02-28 13:28

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_auto_20210228_1812'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='leagueteam',
            options={'ordering': ('-points',)},
        ),
        migrations.AddField(
            model_name='leagueteam',
            name='logo_url',
            field=models.URLField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
