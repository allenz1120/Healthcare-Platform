# Generated by Django 4.0.2 on 2022-02-17 16:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0009_rename_insurance_comapny_billing_insurance_comapany'),
    ]

    operations = [
        migrations.RenameField(
            model_name='billing',
            old_name='insurance_comapany',
            new_name='insurance_company',
        ),
    ]
