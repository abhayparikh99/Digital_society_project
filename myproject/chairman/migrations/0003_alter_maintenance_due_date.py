# Generated by Django 3.2.4 on 2021-07-31 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chairman', '0002_alter_memberdetails_job_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maintenance',
            name='due_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]