# Generated by Django 3.2.7 on 2021-10-01 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0004_auto_20210927_2057'),
    ]

    operations = [
        migrations.RenameField(
            model_name='drinkmenuitem',
            old_name='price',
            new_name='price01',
        ),
        migrations.AddField(
            model_name='drinkmenuitem',
            name='price02',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True),
        ),
        migrations.AddField(
            model_name='drinkmenuitem',
            name='price03',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True),
        ),
    ]
