# Generated by Django 3.2.5 on 2022-02-07 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signalapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_user', models.CharField(default='', max_length=120)),
            ],
        ),
    ]