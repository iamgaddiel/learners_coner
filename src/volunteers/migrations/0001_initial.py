# Generated by Django 3.1.7 on 2021-04-02 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Volunteer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone_number', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=5)),
                ('title', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=50)),
                ('age', models.PositiveIntegerField()),
                ('degree', models.CharField(max_length=50)),
                ('other_degree', models.CharField(max_length=50)),
                ('work_mode', models.CharField(max_length=50)),
                ('skillsets', models.CharField(max_length=250)),
                ('learn_about_us', models.CharField(max_length=50)),
            ],
        ),
    ]