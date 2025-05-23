# Generated by Django 5.2 on 2025-04-06 14:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='mdlGeo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=100)),
                ('region', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='mdlPCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=100)),
                ('subcategory', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='mdlPCharter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_phase', models.CharField(max_length=200)),
                ('project_owner', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=500)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('budget', models.DecimalField(decimal_places=2, max_digits=10)),
                ('human_resources', models.IntegerField()),
                ('stage', models.CharField(choices=[('A', 'Approved'), ('O', 'Ongoing'), ('T', 'Terminated')], max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='mdlPDeliverable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deliverable_name', models.CharField(max_length=500)),
                ('content_type', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=200)),
                ('authors', models.CharField(max_length=200)),
                ('published_date', models.DateField()),
                ('description', models.CharField(max_length=500)),
                ('url', models.URLField()),
                ('project_phase', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='s2app.mdlpcharter')),
            ],
        ),
        migrations.CreateModel(
            name='mdlProject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project', models.CharField(max_length=200)),
                ('year', models.CharField(max_length=4)),
                ('budget', models.DecimalField(decimal_places=2, max_digits=10)),
                ('outcome', models.CharField(choices=[('S', 'Success'), ('F', 'Failure'), ('O', 'Ongoing')], max_length=100)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='s2app.mdlgeo')),
                ('subcategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='s2app.mdlpcategory')),
            ],
        ),
        migrations.AddField(
            model_name='mdlpcharter',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='s2app.mdlproject'),
        ),
    ]
