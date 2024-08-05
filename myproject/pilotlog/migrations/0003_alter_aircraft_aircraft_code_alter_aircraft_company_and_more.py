# Generated by Django 4.2.10 on 2024-08-05 12:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pilotlog', '0002_aircraft_delete_pilotlog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aircraft',
            name='aircraft_code',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='aircraft',
            name='company',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='aircraft',
            name='fin',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='aircraft',
            name='guid',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='aircraft',
            name='make',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='aircraft',
            name='model',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='aircraft',
            name='modified',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='aircraft',
            name='rating',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='aircraft',
            name='ref_search',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='aircraft',
            name='reference',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='aircraft',
            name='sub_model',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flight_id', models.CharField(max_length=255)),
                ('departure_time', models.DateTimeField()),
                ('arrival_time', models.DateTimeField()),
                ('origin', models.CharField(blank=True, default='', max_length=255)),
                ('destination', models.CharField(blank=True, default='', max_length=255)),
                ('pilot', models.CharField(blank=True, default='', max_length=255)),
                ('duration', models.DurationField()),
                ('remarks', models.TextField(blank=True, default='')),
                ('aircraft', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pilotlog.aircraft')),
            ],
        ),
    ]