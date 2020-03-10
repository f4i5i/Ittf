# Generated by Django 3.0.4 on 2020-03-10 20:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Phases',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=100)),
                ('desc', models.CharField(max_length=200)),
                ('evkey', models.CharField(max_length=100)),
                ('phase_type', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='RawData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('raw_data', models.TextField(max_length=10000)),
            ],
        ),
        migrations.CreateModel(
            name='Table',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=100)),
                ('desc', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Competition',
            fields=[
                ('champ', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('description', models.TextField(max_length=1000)),
                ('location', models.TextField(max_length=1000)),
                ('isfinished', models.BooleanField()),
                ('url', models.URLField(max_length=1000)),
                ('phase_comp', models.ManyToManyField(blank=True, related_name='competition_phases', to='tabletennis.Phases')),
                ('raw_comp', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='competition_rawdata', to='tabletennis.RawData')),
                ('table_comp', models.ManyToManyField(blank=True, related_name='competition_table', to='tabletennis.Table')),
            ],
        ),
    ]
