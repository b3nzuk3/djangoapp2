# Generated by Django 4.0.5 on 2022-06-08 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imageGram', '0005_alter_image_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
