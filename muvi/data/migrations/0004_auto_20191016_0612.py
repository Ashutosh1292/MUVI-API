# Generated by Django 2.2.4 on 2019-10-16 00:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0003_auto_20191016_0609'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='alie_customer_id',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='content',
            name='movie_id',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='content',
            name='store_id',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
