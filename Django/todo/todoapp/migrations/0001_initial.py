# Generated by Django 4.1.5 on 2023-06-07 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=1000)),
                ('due_date', models.DateField(blank=True, null=True)),
                ('status', models.CharField(choices=[('OPEN', 'Open'), ('WORKING', 'Working'), ('DONE', 'Done'), ('OVERDUE', 'Overdue')], default='OPEN', max_length=10)),
                ('tags', models.ManyToManyField(blank=True, to='todoapp.tag')),
            ],
        ),
    ]
