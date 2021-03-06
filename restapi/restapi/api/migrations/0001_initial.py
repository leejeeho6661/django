# Generated by Django 3.1.7 on 2021-03-18 01:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=20)),
                ('weekend', models.CharField(max_length=20)),
                ('gross', models.CharField(max_length=20)),
                ('weeks', models.CharField(max_length=20)),
                ('genre', models.CharField(max_length=100)),
                ('rating', models.CharField(max_length=10)),
                ('movie_release', models.CharField(max_length=20)),
                ('people', models.CharField(max_length=20)),
                ('created_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'movie',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MyTopicMovie',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.TextField()),
                ('weekend', models.TextField()),
                ('gross', models.TextField()),
                ('weeks', models.TextField()),
                ('genre', models.TextField()),
                ('rating', models.TextField()),
                ('movie_release', models.TextField()),
                ('people', models.TextField()),
                ('created_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'my_topic_movie',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MyTopicUsers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('weekend', models.TextField()),
                ('gross', models.TextField()),
                ('weeks', models.TextField()),
                ('genre', models.TextField()),
                ('rating', models.TextField()),
                ('movie_release', models.TextField()),
                ('people', models.TextField()),
                ('created_at', models.DateTimeField()),
            ],
            options={
                'db_table': 'my_topic_users',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stock_rank', models.CharField(max_length=20)),
                ('title', models.CharField(max_length=50)),
                ('price', models.CharField(max_length=20)),
                ('ratio_updown', models.CharField(max_length=5)),
                ('ratio', models.CharField(max_length=10)),
                ('low', models.CharField(max_length=10)),
                ('volume', models.CharField(max_length=10)),
                ('payment', models.CharField(max_length=20)),
                ('buy', models.CharField(max_length=20)),
                ('sell', models.CharField(max_length=20)),
                ('capitalization', models.CharField(max_length=20)),
                ('per', models.CharField(max_length=20)),
                ('roe', models.CharField(max_length=20)),
                ('created_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'stock',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TopicStock',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('stock_rank', models.TextField()),
                ('title', models.TextField()),
                ('price', models.TextField()),
                ('low', models.TextField()),
                ('volume', models.TextField()),
                ('payment', models.TextField()),
                ('buy', models.TextField()),
                ('sell', models.TextField()),
                ('capitalization', models.TextField()),
                ('per', models.TextField()),
                ('roe', models.TextField()),
                ('created_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'topic_stock',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('weekend', models.CharField(max_length=20)),
                ('gross', models.CharField(max_length=20)),
                ('weeks', models.CharField(max_length=20)),
                ('genre', models.CharField(max_length=100)),
                ('movie_release', models.CharField(max_length=20)),
                ('rating', models.CharField(max_length=10)),
                ('people', models.CharField(max_length=20)),
                ('created_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'users',
                'managed': False,
            },
        ),
    ]
