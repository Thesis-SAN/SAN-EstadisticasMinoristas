# Generated by Django 3.2.8 on 2022-11-28 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estad_minoristas', '0004_auto_20221128_0856'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='n_familia',
            name='id',
        ),
        migrations.AlterField(
            model_name='n_familia',
            name='fam_id_oltp',
            field=models.CharField(max_length=10, primary_key=True, serialize=False),
        ),
    ]
