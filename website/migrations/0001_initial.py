# Generated by Django 4.2.4 on 2023-08-10 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=30)),
                ('phone', models.CharField(max_length=15)),
                ('town', models.CharField(max_length=20)),
                ('po', models.CharField(max_length=20)),
                ('dist', models.CharField(max_length=20)),
                ('state', models.CharField(max_length=20)),
                ('pin', models.CharField(max_length=10)),
            ],
        ),
    ]
