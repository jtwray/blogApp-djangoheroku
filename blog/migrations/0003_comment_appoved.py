# Generated by Django 2.1.3 on 2018-12-27 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='appoved',
            field=models.BooleanField(default=False),
        ),
    ]
