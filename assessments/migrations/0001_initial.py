# Generated by Django 4.1.1 on 2023-02-20 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='videoAns',
            fields=[
                ('ansId', models.AutoField(primary_key=True, serialize=False)),
                ('user_name', models.CharField(max_length=255, null=True)),
                ('assessment_name', models.CharField(max_length=300, null=True)),
                ('videoAns', models.FileField(blank=True, upload_to='media')),
                ('trasnscript', models.CharField(max_length=10000, null=True)),
            ],
        ),
    ]