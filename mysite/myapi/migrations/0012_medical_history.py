# Generated by Django 4.0.2 on 2022-03-02 17:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0011_alter_billing_credit_card_alter_billing_cvv_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Medical_History',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('family_predisposition', models.CharField(max_length=100)),
                ('allergies', models.CharField(max_length=50)),
                ('medication', models.CharField(max_length=100)),
                ('drinking', models.BooleanField()),
                ('smoking', models.BooleanField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapi.users')),
            ],
        ),
    ]