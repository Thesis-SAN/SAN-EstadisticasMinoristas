# Generated by Django 3.2.8 on 2022-11-28 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estad_minoristas', '0005_auto_20221128_1131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='n_familia',
            name='fam_id_oltp',
            field=models.CharField(default='', max_length=10, primary_key=True, serialize=False),
        ),
    ]
