# Generated by Django 3.2.14 on 2022-07-29 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('argonapp', '0009_amenities'),
    ]

    operations = [
        migrations.CreateModel(
            name='Nearby_Landmark',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('status', models.BooleanField(default=False)),
                ('deleted', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]