# Generated by Django 4.0.4 on 2022-05-02 00:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_write_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='write',
            name='user',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
        migrations.DeleteModel(
            name='Write',
        ),
    ]
