# Generated by Django 3.0.2 on 2020-08-30 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='face_photos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img_input', models.ImageField(default='default.png', upload_to='images_input/')),
                ('img_output', models.ImageField(default='default.png', upload_to='images_output/')),
            ],
        ),
    ]
