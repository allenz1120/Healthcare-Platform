# Generated by Django 4.0.2 on 2022-03-17 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0015_delete_roles'),
    ]

    operations = [
        migrations.CreateModel(
            name='Roles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rid', models.IntegerField()),
                ('role', models.CharField(max_length=15)),
            ],
        ),
    ]