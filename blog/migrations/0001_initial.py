# Generated by Django 3.2.8 on 2021-10-20 06:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='kategori',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Artikel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(blank=True, max_length=100, null=True)),
                ('judul', models.CharField(max_length=100)),
                ('body', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('kategori', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='blog.kategori')),
            ],
        ),
    ]
