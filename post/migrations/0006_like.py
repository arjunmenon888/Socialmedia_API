# Generated by Django 3.1.1 on 2020-10-02 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0005_auto_20201002_2220'),
    ]

    operations = [
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Vote', models.CharField(blank=True, choices=[('a', 'a'), ('b', 'b'), ('c', 'c')], max_length=1, null=True)),
            ],
        ),
    ]