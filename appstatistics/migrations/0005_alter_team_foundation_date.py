# Generated by Django 4.1.5 on 2023-03-02 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appstatistics', '0004_remove_team_date_foundation_remove_team_team_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='foundation_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
