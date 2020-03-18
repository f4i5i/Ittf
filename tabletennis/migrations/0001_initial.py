# Generated by Django 3.0.4 on 2020-03-18 08:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Competition',
            fields=[
                ('champ', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('description', models.TextField(max_length=1000)),
                ('location', models.TextField(max_length=1000)),
                ('isfinished', models.BooleanField()),
                ('url', models.URLField(max_length=1000)),
                ('compdates', models.TextField(max_length=1000)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('short_name', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Missingdata',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('home', models.CharField(max_length=300)),
                ('away', models.CharField(max_length=300)),
                ('url', models.URLField(max_length=300)),
                ('phase', models.CharField(max_length=300)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Phases',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=100)),
                ('desc', models.CharField(max_length=200)),
                ('evkey', models.CharField(max_length=100)),
                ('phase_type', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('player_id', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('name', models.TextField(max_length=1000)),
                ('gender', models.CharField(max_length=50)),
                ('dob', models.CharField(blank=True, max_length=100, null=True)),
                ('activity', models.CharField(max_length=100)),
                ('sport', models.CharField(default='Table Tennis', max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('org', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='country', to='tabletennis.Country')),
            ],
        ),
        migrations.CreateModel(
            name='RawData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('raw_data', models.TextField(max_length=10000)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Table',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=100)),
                ('desc', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('team_id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('player1', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='player_1', to='tabletennis.Player')),
                ('player2', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='player_2', to='tabletennis.Player')),
            ],
        ),
        migrations.CreateModel(
            name='MatchRawData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(max_length=1000)),
                ('json_data', models.TextField(max_length=50000)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('comp', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='competition', to='tabletennis.Competition')),
            ],
        ),
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('match', models.CharField(max_length=200)),
                ('time', models.CharField(max_length=100)),
                ('venue', models.CharField(max_length=250)),
                ('status', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('away', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='away', to='tabletennis.Player')),
                ('comp', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='champ_competition', to='tabletennis.Competition')),
                ('home', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='home', to='tabletennis.Player')),
                ('phase', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='match_phase', to='tabletennis.Phases')),
                ('table', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='loc', to='tabletennis.Table')),
                ('team_away', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='teams_away', to='tabletennis.Team')),
                ('team_home', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='teams_home', to='tabletennis.Team')),
            ],
        ),
        migrations.CreateModel(
            name='DeletedFixture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fixture', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='tabletennis.Match')),
            ],
        ),
        migrations.AddField(
            model_name='competition',
            name='raw_comp',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='competition_rawdata', to='tabletennis.RawData'),
        ),
    ]
