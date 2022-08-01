# Generated by Django 4.0.3 on 2022-04-11 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='logintable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=25)),
                ('second_name', models.CharField(max_length=25)),
                ('username', models.CharField(max_length=25)),
                ('gender', models.CharField(choices=[('m', 'male'), ('f', 'female')], max_length=10)),
                ('password', models.CharField(max_length=36)),
                ('email', models.EmailField(max_length=254)),
                ('datetime', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'pro1',
            },
        ),
    ]
