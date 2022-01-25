# Generated by Django 3.1.14 on 2022-01-25 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='detailmodel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=30)),
                ('Age', models.IntegerField()),
                ('Mobile', models.IntegerField()),
                ('Email', models.EmailField(max_length=254)),
                ('Qualification', models.CharField(choices=[('MCA', 'MCA'), ('Mcom', 'Mcom'), ('B.Tech', 'B.Tech'), ('CA', 'CA')], max_length=30)),
                ('Branch', models.CharField(choices=[('M.s.cs', 'M.s.cs'), ('M.p.cs', 'M.p.cs'), ('B.com', 'B.com'), ('B.z.c', 'B.z.c')], max_length=30)),
                ('Exam', models.CharField(choices=[('Computer', 'Computer'), ('Non-Computer', 'Non-Computer')], max_length=30)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='exammodel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=30)),
                ('Age', models.IntegerField()),
                ('Mobile', models.IntegerField()),
                ('Email', models.EmailField(max_length=254)),
                ('Qualification', models.CharField(choices=[('MCA', 'MCA'), ('Mcom', 'Mcom'), ('B.Tech', 'B.Tech'), ('CA', 'CA')], max_length=30)),
                ('Branch', models.CharField(choices=[('M.s.cs', 'M.s.cs'), ('M.p.cs', 'M.p.cs'), ('B.com', 'B.com'), ('B.z.c', 'B.z.c')], max_length=30)),
                ('Exam_Type', models.CharField(choices=[('Online', 'Online'), ('Offline', 'Offline')], max_length=30)),
                ('Time', models.TimeField()),
                ('Feedback', models.TextField(default='Write Something For heare....')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
