# Generated by Django 3.2.3 on 2021-05-31 13:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog_api', '0005_auto_20210531_1315'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'category', 'verbose_name_plural': 'categories'},
        ),
    ]