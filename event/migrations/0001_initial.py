# Generated by Django 4.2 on 2023-04-18 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dept', models.CharField(max_length=20)),
                ('num', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=50)),
                ('photo', models.ImageField(upload_to='img/')),
            ],
        ),
    ]