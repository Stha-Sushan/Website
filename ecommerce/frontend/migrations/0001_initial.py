# Generated by Django 4.1.3 on 2022-11-14 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cname', models.CharField(max_length=255)),
                ('Description', models.CharField(max_length=255)),
                ('status', models.BooleanField()),
            ],
        ),
    ]
