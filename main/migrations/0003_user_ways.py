# Generated by Django 3.2.8 on 2021-10-21 05:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_logicquiz_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='ways',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='way_users', to='main.ways'),
        ),
    ]