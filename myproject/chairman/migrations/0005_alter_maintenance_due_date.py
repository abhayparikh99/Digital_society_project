# Generated by Django 3.2.4 on 2021-08-21 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chairman', '0004_alter_maintenance_due_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maintenance',
            name='due_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
