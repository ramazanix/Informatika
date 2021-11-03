# Generated by Django 3.2.8 on 2021-10-30 15:33

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('body', models.TextField(max_length=2500)),
                ('publication_date', models.DateTimeField(default=datetime.datetime(2021, 10, 30, 15, 33, 58, 817392, tzinfo=utc), editable=False)),
                ('author', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='users.userprofile')),
            ],
        ),
        migrations.CreateModel(
            name='ImagesForPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='posts_images')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.post')),
            ],
        ),
    ]
