# Generated by Django 3.0.4 on 2020-04-22 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='timeStamp',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='timeStamp',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='timeStamp',
            field=models.DateField(blank=True),
        ),
    ]
