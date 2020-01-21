# Generated by Django 3.0 on 2020-01-09 08:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Engineer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Alias', models.CharField(max_length=10)),
                ('Name', models.CharField(max_length=20)),
                ('EngineerLatestProcess', models.BigIntegerField(default=-1)),
                ('EngineerLatestStage', models.BigIntegerField(default=-1)),
                ('IsReviewer', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='EngineerTitle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FullName', models.CharField(max_length=20)),
                ('Abbreviation', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Process',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Stage1TryTimes', models.BigIntegerField(default=-1)),
                ('Stage2TryTimes', models.BigIntegerField(default=-1)),
                ('Stage3TryTimes', models.BigIntegerField(default=-1)),
                ('Stage4TryTimes', models.BigIntegerField(default=-1)),
            ],
        ),
        migrations.CreateModel(
            name='ProcessKind',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FullName', models.CharField(max_length=20)),
                ('Abbreviation', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='StageKind',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FullName', models.CharField(max_length=20)),
                ('Abbreviation', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Reviewer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Alias', models.CharField(max_length=10)),
                ('Name', models.CharField(max_length=20)),
                ('Title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='escBackend.EngineerTitle')),
            ],
        ),
        migrations.CreateModel(
            name='ProcessReview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Process', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='escBackend.Process')),
                ('Reviewer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='escBackend.Reviewer')),
            ],
        ),
        migrations.AddField(
            model_name='process',
            name='Kind',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='escBackend.ProcessKind'),
        ),
        migrations.AddField(
            model_name='process',
            name='ProcessCurrentStage',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='escBackend.StageKind'),
        ),
        migrations.AddField(
            model_name='process',
            name='ProcessOwner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='escBackend.Engineer'),
        ),
        migrations.AddField(
            model_name='process',
            name='ProcessReviewer',
            field=models.ManyToManyField(through='escBackend.ProcessReview', to='escBackend.Reviewer'),
        ),
        migrations.AddField(
            model_name='engineer',
            name='Title',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='escBackend.EngineerTitle'),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Edited', models.BooleanField(default=False)),
                ('Submited', models.BooleanField(default=False)),
                ('Process', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='escBackend.Process')),
                ('Stage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='escBackend.StageKind')),
                ('Writer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='escBackend.Reviewer')),
            ],
        ),
    ]
