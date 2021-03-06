# Generated by Django 3.2.7 on 2021-09-27 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_drinkmenuitem_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='drinkmenuitem',
            name='item_id',
        ),
        migrations.RemoveField(
            model_name='foodmenuitem',
            name='item_id',
        ),
        migrations.AlterField(
            model_name='drinkmenuitem',
            name='category',
            field=models.CharField(choices=[('SOFT', 'Soft drink'), ('HOT', 'Hot drink'), ('BEER', 'Beer'), ('WHITE_WINE', 'White wine'), ('RED_WINE', 'Red wine'), ('CAKTAIL', 'Caktail'), ('SAKE', 'Sake'), ('OTHER', 'Other'), ('SPECIAL', 'Special')], max_length=50),
        ),
        migrations.AlterField(
            model_name='drinkmenuitem',
            name='item_name',
            field=models.CharField(max_length=100, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='foodmenuitem',
            name='category',
            field=models.CharField(choices=[('TAPAS', 'Tapas'), ('NOODLE', 'Noodle'), ('RICE', 'Rice'), ('SPECIAL', 'Special')], max_length=50),
        ),
        migrations.AlterField(
            model_name='foodmenuitem',
            name='item_name',
            field=models.CharField(max_length=100, primary_key=True, serialize=False),
        ),
    ]
