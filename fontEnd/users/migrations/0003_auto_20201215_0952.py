# Generated by Django 3.1.2 on 2020-12-15 04:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_remove_appuser_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(default=True, max_length=50, null=True, unique=True)),
                ('password', models.CharField(default=True, max_length=50, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Appuser',
        ),
    ]