# Generated by Django 2.1.15 on 2020-04-03 02:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quote', '0003_auto_20200403_1017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='current_status',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='dept',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='employe',
            name='employe_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
