# Generated by Django 4.1.2 on 2022-11-28 18:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('printing3d', '0004_alter_model3d_image_path'),
    ]

    operations = [
        migrations.AlterField(
            model_name='model3d',
            name='image_path',
            field=models.ImageField(upload_to='images', verbose_name='Фото модели'),
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_model', models.ForeignKey(db_column='model', on_delete=django.db.models.deletion.DO_NOTHING, to='printing3d.model3d', verbose_name='Модель')),
                ('id_user', models.ForeignKey(db_column='user', on_delete=django.db.models.deletion.DO_NOTHING, to='printing3d.user3d', verbose_name='Пользователь')),
            ],
        ),
    ]
