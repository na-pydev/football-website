# Generated by Django 3.1.5 on 2021-02-27 04:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20210227_0901'),
    ]

    operations = [
        migrations.AddField(
            model_name='match',
            name='previous_match',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='match',
            name='date',
            field=models.DateTimeField(),
        ),
    ]
