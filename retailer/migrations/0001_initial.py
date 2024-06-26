# Generated by Django 4.1.7 on 2024-05-14 17:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bought',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('owner', models.CharField(max_length=30)),
                ('type', models.CharField(max_length=30)),
                ('company', models.CharField(max_length=30)),
                ('price', models.CharField(max_length=30)),
                ('quantity', models.CharField(max_length=30)),
                ('boughtquantity', models.CharField(max_length=30)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.user')),
            ],
        ),
    ]
