# Generated by Django 4.0.6 on 2022-08-04 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_review'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
            ],
        ),
        migrations.AddField(
            model_name='movie',
            name='category',
            field=models.CharField(default='Uncategorized', max_length=300),
        ),
    ]
