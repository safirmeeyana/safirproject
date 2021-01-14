# Generated by Django 3.1.5 on 2021-01-12 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='place',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=150)),
                ('Image', models.ImageField(upload_to='picture')),
                ('Description', models.TextField()),
                ('Price', models.IntegerField()),
                ('Offer', models.BooleanField(default=False)),
            ],
        ),
    ]
