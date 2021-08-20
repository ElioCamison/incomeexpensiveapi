# Generated by Django 3.2.6 on 2021-08-20 18:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=32)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=15)),
                ('description', models.TextField(blank=True)),
                ('date', models.DateTimeField()),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='categories', to='expenses.category')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='owner', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
