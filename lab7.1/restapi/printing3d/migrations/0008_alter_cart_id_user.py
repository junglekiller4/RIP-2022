# Generated by Django 4.1.2 on 2022-12-07 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('printing3d', '0007_user3d_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='id_user',
            field=models.IntegerField(verbose_name='Пользователь'),
        ),
    ]
