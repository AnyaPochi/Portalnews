# Generated by Django 4.2.9 on 2024-02-19 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='type',
            field=models.CharField(choices=[(1, 'Статья'), (2, 'Новость')], default='Новость', max_length=20),
        ),
    ]