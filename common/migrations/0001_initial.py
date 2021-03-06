# Generated by Django 2.1.5 on 2020-07-27 16:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('body', models.TextField()),
                ('time', models.DateTimeField()),
                ('status', models.PositiveSmallIntegerField(choices=[(1, 'sent'), (2, 'wait')])),
                ('email', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common.Email')),
            ],
        ),
    ]
