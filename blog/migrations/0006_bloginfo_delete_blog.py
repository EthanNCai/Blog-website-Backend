# Generated by Django 4.2.7 on 2023-11-26 12:13

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_blog_delete_blog_info'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogInfo',
            fields=[
                ('blog_id', models.AutoField(primary_key=True, serialize=False)),
                ('blog_name', models.CharField(max_length=50)),
                ('blog_likes', models.IntegerField(default=0)),
                ('blog_hates', models.IntegerField(default=0)),
                ('blog_date', models.DateField(default=django.utils.timezone.now)),
                ('blog_category', models.CharField(max_length=50)),
                ('blog_description', models.CharField(max_length=200)),
            ],
        ),
        migrations.DeleteModel(
            name='Blog',
        ),
    ]