# Generated by Django 4.2.1 on 2023-06-02 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ftb', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='flight',
            name='uniquename',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
