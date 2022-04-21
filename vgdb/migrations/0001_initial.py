# Generated by Django 4.0.4 on 2022-04-21 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('about', models.CharField(max_length=2000)),
                ('perspective', models.CharField(max_length=50)),
                ('release_date', models.DateField(null=True)),
                ('coverart', models.URLField(max_length=500)),
                ('expansions', models.CharField(max_length=200)),
            ],
        ),
    ]