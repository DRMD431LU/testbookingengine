# Generated by Django 4.0.2 on 2022-02-21 18:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pms', '0011_alter_book_code'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(choices=[('NEW', 'Nueva'), ('DEL', 'Cancelada')], default='NEW', max_length=3)),
                ('checkin', models.DateField()),
                ('checkout', models.DateField()),
                ('guests', models.IntegerField()),
                ('total', models.FloatField()),
                ('code', models.CharField(default='J3X67E6W', max_length=8)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='pms.customer')),
                ('room', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='pms.room')),
            ],
        ),
        migrations.DeleteModel(
            name='Book',
        ),
    ]