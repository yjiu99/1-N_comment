# Generated by Django 3.2.7 on 2021-09-27 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commentapp', '0006_comment_pub_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='pub_date',
        ),
        migrations.AddField(
            model_name='comment',
            name='date',
            field=models.DateField(null=True),
        ),
    ]