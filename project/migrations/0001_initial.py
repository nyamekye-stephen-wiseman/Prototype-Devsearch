# Generated by Django 4.0.4 on 2022-05-22 16:32

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('created_date', models.DateTimeField(auto_now=True)),
                ('modification_date', models.DateTimeField(auto_now_add=True)),
                ('project_img', models.ImageField(blank=True, default='default.jpg', null=True, upload_to='')),
                ('source_code_url', models.CharField(blank=True, max_length=500, null=True)),
                ('demo_code_url', models.CharField(blank=True, max_length=500, null=True)),
                ('vote_total', models.IntegerField(blank=True, default=0, null=True)),
                ('vote_ratio', models.IntegerField(blank=True, default=0, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('created_date', models.DateTimeField(auto_now=True)),
                ('modification_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('up_vote', models.CharField(choices=[('up', 'Up Vote'), ('dw', 'Down Vote')], max_length=2)),
                ('down_vote', models.CharField(choices=[('up', 'Up Vote'), ('dw', 'Down Vote')], max_length=2)),
                ('created_date', models.DateTimeField(auto_now=True)),
                ('modification_date', models.DateTimeField(auto_now_add=True)),
                ('project', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='project.project')),
            ],
        ),
        migrations.AddField(
            model_name='project',
            name='tags',
            field=models.ManyToManyField(blank=True, null=True, to='project.tags'),
        ),
    ]
