# Generated by Django 4.0.4 on 2023-03-26 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0002_images_alter_employee_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vectors',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('id_user', models.CharField(max_length=255)),
                ('vector', models.TextField()),
            ],
        ),
    ]