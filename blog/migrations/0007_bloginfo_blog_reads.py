# Generated by Django 4.2.7 on 2023-11-26 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_bloginfo_delete_blog'),
    ]

    operations = [
        migrations.AddField(
            model_name='bloginfo',
            name='blog_reads',
            field=models.IntegerField(default=0),
        ),
    ]
