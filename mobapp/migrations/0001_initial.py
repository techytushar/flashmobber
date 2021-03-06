# Generated by Django 2.0.4 on 2018-05-01 08:36

from django.db import migrations, models
import mobapp.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('year', models.IntegerField(default=mobapp.models.this_year)),
                ('slug', models.SlugField(unique=True)),
            ],
            options={
                'ordering': ['-year', 'name'],
            },
        ),
    ]
