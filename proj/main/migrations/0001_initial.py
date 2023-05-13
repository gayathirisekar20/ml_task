# Generated by Django 3.2.19 on 2023-05-10 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cereal',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('mrf', models.CharField(max_length=10)),
                ('type', models.CharField(max_length=10)),
                ('calories', models.FloatField(default=0)),
                ('protein', models.FloatField(default=0)),
                ('fat', models.IntegerField(default=0)),
                ('sodium', models.IntegerField(default=0)),
                ('fiber', models.FloatField(default=0)),
                ('carbo', models.FloatField(default=0)),
                ('sugars', models.IntegerField(default=0)),
                ('potass', models.IntegerField(default=0)),
                ('vitamins', models.IntegerField(default=0)),
                ('shelf', models.IntegerField(default=0)),
                ('weight', models.FloatField(default=0)),
                ('cups', models.FloatField(default=0)),
                ('rating', models.FloatField(default=0)),
                ('procal', models.IntegerField(default=0)),
            ],
        ),
    ]
