# Generated by Django 3.0.2 on 2020-01-20 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WebsiteContects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('websection', models.CharField(default='', max_length=255)),
                ('heading1', models.CharField(default='', max_length=255)),
                ('heading2', models.CharField(default='', max_length=255)),
                ('description', models.CharField(default='', max_length=255)),
                ('attachment_image', models.ImageField(default='', upload_to='assets/img/website')),
                ('attachment_file', models.FileField(default='', upload_to='assets/uploads/website')),
                ('datafeatured', models.CharField(default='', max_length=255)),
            ],
        ),
    ]
