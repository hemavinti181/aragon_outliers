# Generated by Django 3.2.14 on 2022-07-24 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('argonapp', '0002_alter_country_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='country',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='country',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]