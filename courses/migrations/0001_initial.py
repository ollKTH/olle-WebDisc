# Generated by Django 2.1.2 on 2018-12-22 19:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=255)),
                ('num_of_holes', models.PositiveIntegerField()),
                ('sun_hours', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Hole',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('par', models.PositiveIntegerField()),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.Course')),
            ],
        ),
        migrations.CreateModel(
            name='HoleRoundLink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hole', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.Hole')),
            ],
        ),
        migrations.CreateModel(
            name='Round',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_par', models.PositiveIntegerField()),
                ('num_of_holes', models.PositiveIntegerField()),
                ('highscore', models.PositiveIntegerField()),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.Course')),
            ],
        ),
        migrations.AddField(
            model_name='holeroundlink',
            name='round',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.Round'),
        ),
        migrations.AddField(
            model_name='hole',
            name='round',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.Round'),
        ),
    ]
