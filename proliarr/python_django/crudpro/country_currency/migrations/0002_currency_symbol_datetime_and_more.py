# Generated by Django 4.0.3 on 2022-04-06 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('country_currency', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='currency_symbol',
            name='datetime',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='currency_symbol',
            name='currency_symbol',
            field=models.CharField(max_length=50),
        ),
    ]
