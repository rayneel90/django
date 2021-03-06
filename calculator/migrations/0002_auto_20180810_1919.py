# Generated by Django 2.0.5 on 2018-08-10 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calculator', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='query',
            name='updated',
        ),
        migrations.AlterField(
            model_name='query',
            name='conpay',
            field=models.FloatField(verbose_name='Sourcing Fee'),
        ),
        migrations.AlterField(
            model_name='query',
            name='ltv',
            field=models.FloatField(default=0.0, verbose_name='LTV'),
        ),
        migrations.AlterField(
            model_name='query',
            name='profee',
            field=models.FloatField(verbose_name='Processing Fee'),
        ),
        migrations.AlterField(
            model_name='query',
            name='roi',
            field=models.FloatField(verbose_name='ROI'),
        ),
        migrations.AlterField(
            model_name='query',
            name='utilisation',
            field=models.FloatField(default=70.0, verbose_name='Utilisation'),
        ),
    ]
