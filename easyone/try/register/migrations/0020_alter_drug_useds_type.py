# Generated by Django 3.2.9 on 2021-11-15 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0019_drug_useds'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drug_useds',
            name='type',
            field=models.TextField(choices=[(0, '糖尿病藥物'), (1, '高血壓藥物')], max_length=2, null=True),
        ),
    ]