# Generated by Django 3.2.14 on 2022-07-29 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('argonapp', '0007_auto_20220728_1832'),
    ]

    operations = [
        migrations.AddField(
            model_name='area',
            name='zipcode',
            field=models.TextField(blank=True, max_length=8, null=True),
        ),
    ]
