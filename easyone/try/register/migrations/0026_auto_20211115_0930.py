# Generated by Django 3.2.9 on 2021-11-15 09:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0025_auto_20211115_0926'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alc',
            name='user_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='register.uid'),
        ),
        migrations.AlterField(
            model_name='bloodduck',
            name='user_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='register.uid'),
        ),
        migrations.AlterField(
            model_name='bloodsugar',
            name='user_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='register.uid'),
        ),
        migrations.AlterField(
            model_name='caremessage',
            name='user_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='register.uid'),
        ),
        migrations.AlterField(
            model_name='diet',
            name='user_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='register.uid'),
        ),
        migrations.AlterField(
            model_name='drug_useds',
            name='user_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='register.uid'),
        ),
        migrations.AlterField(
            model_name='medical',
            name='user_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='register.uid'),
        ),
        migrations.AlterField(
            model_name='setting',
            name='user_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='register.uid'),
        ),
        migrations.AlterField(
            model_name='weight',
            name='user_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='register.uid'),
        ),
    ]
