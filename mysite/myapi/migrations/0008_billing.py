# Generated by Django 4.0.2 on 2022-02-17 16:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0007_alter_users_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Billing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('insurance_comapny', models.CharField(max_length=50)),
                ('member_id', models.IntegerField(max_length=50)),
                ('member_name', models.CharField(max_length=50)),
                ('credit_card', models.IntegerField(max_length=16)),
                ('expiration_date', models.DateField()),
                ('cvv', models.IntegerField(max_length=3)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapi.users')),
            ],
        ),
    ]
