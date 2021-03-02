# Generated by Django 3.1.5 on 2021-02-28 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_auto_20210228_1000'),
    ]

    operations = [
        migrations.CreateModel(
            name='Directory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_url', models.URLField()),
                ('role', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('surname', models.CharField(max_length=50)),
                ('rank', models.IntegerField()),
            ],
            options={
                'ordering': ('rank',),
            },
        ),
        migrations.AlterModelOptions(
            name='news',
            options={'ordering': ('-date_added',), 'verbose_name': 'News', 'verbose_name_plural': 'News'},
        ),
    ]