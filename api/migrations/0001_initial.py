# Generated by Django 4.1.1 on 2023-04-26 01:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('added_date', models.DateTimeField(auto_created=True)),
                ('company_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=50)),
                ('about', models.TextField()),
                ('type', models.CharField(choices=[('IT', 'IT'), ('Non IT', 'None IT')], max_length=100)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
    ]
