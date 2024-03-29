# Generated by Django 3.2.4 on 2021-11-08 19:53

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.CharField(editable=False, max_length=20, unique=True)),
                ('password', models.CharField(max_length=100)),
                ('posts_written', models.IntegerField(default=0)),
                ('last_login', models.DateTimeField(default=datetime.datetime(2021, 11, 8, 19, 53, 35, 296404, tzinfo=utc), editable=False)),
                ('join_date', models.DateTimeField(default=datetime.datetime(2021, 11, 8, 19, 53, 35, 296444, tzinfo=utc), editable=False)),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='user', max_length=20)),
                ('description', models.CharField(default='standard user', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('user', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='users.customuser')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(blank=True, max_length=35)),
                ('photo', models.ImageField(default='default_avatar/1.png', upload_to='user_avatars/')),
            ],
        ),
        migrations.AddField(
            model_name='customuser',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='users.group'),
        ),
    ]
