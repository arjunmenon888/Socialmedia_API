# Generated by Django 3.1.1 on 2020-10-02 20:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0006_like'),
    ]

    operations = [
        migrations.RenameField(
            model_name='like',
            old_name='Vote',
            new_name='vote',
        ),
    ]