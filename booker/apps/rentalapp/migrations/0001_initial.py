# Generated by Django 2.2.17 on 2020-11-26 23:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('libraryapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.DecimalField(decimal_places=2, max_digits=50)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-timestamp'],
            },
        ),
        migrations.CreateModel(
            name='RentItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('stop_date', models.DateField()),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='libraryapp.Book')),
                ('rent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rentalapp.Rent')),
            ],
        ),
        migrations.AddField(
            model_name='rent',
            name='items',
            field=models.ManyToManyField(through='rentalapp.RentItem', to='libraryapp.Book'),
        ),
    ]