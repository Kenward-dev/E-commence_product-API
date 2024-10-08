# Generated by Django 5.1.1 on 2024-09-30 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('P', 'Pending'), ('C', 'Completed'), ('X', 'Cancelled'), ('R', 'Returned')], default='P', max_length=1),
        ),
    ]
