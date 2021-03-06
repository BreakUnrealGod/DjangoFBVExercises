# Generated by Django 2.2.3 on 2019-07-08 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vip', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vip',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
        migrations.AlterField(
            model_name='permission',
            name='name',
            field=models.CharField(max_length=32, unique=True),
        ),
        migrations.AlterField(
            model_name='vip',
            name='level',
            field=models.IntegerField(unique=True),
        ),
        migrations.AlterField(
            model_name='vip',
            name='name',
            field=models.CharField(max_length=32, unique=True),
        ),
    ]
