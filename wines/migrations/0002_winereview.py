# Generated by Django 3.2 on 2022-11-17 13:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wines', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='WineReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('rating', models.IntegerField(choices=[(0, '0 stars'), (1, '1 stars'), (2, '2 stars'), (3, '3 stars'), (4, '4 stars'), (5, '5 stars')], default=0)),
                ('is_customer', models.BooleanField(blank=True, default=False, null=True)),
                ('review', models.TextField()),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('status', models.IntegerField(choices=[(0, 'Draft'), (1, 'Published')], default=0)),
                ('wine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='wines.wine')),
            ],
            options={
                'ordering': ['date_created'],
            },
        ),
    ]
