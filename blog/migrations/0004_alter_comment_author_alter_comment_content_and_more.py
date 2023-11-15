# Generated by Django 4.2.3 on 2023-11-14 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_comment_alter_post_date_posted_delete_comments_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='author',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='comment',
            name='content',
            field=models.TextField(max_length=500),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date_posted',
            field=models.CharField(default='2023-11-14 19:25', max_length=70),
        ),
        migrations.AlterField(
            model_name='post',
            name='date_posted',
            field=models.CharField(default='2023-11-14 19:25', max_length=70),
        ),
    ]