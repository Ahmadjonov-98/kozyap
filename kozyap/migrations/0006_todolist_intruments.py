# Generated by Django 4.1.3 on 2022-11-25 17:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('kozyap', '0005_staff_brigadier_alter_staffreport_stuff_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='ToDoList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Sana')),
                ('stuff_count', models.IntegerField(verbose_name='Hodimlar Soni')),
                ('todos', models.TextField(verbose_name='Qilingan Ishlar')),
                ('comment', models.TextField(null=True, verbose_name='Izoh')),
                ('measure', models.CharField(max_length=56, null=True, verbose_name="O'lchov birligi")),
                ('size', models.CharField(max_length=128, null=True, verbose_name='Qilingan ish obyomi')),
                ('price', models.IntegerField(null=True, verbose_name='Narxi')),
                ('total', models.IntegerField(null=True, verbose_name='Jami')),
                ('admin_comment', models.TextField(null=True, verbose_name='Admin Izohi')),
                ('brigadier', models.ForeignKey(default=-1, on_delete=django.db.models.deletion.SET_DEFAULT, to='kozyap.brigadier', verbose_name='Brigadir')),
                ('object', models.ForeignKey(default=-1, on_delete=django.db.models.deletion.SET_DEFAULT, to='kozyap.object', verbose_name='Obyekt')),
            ],
            options={
                'verbose_name': "Qilinga Ish Qo'shish",
                'verbose_name_plural': "Qilingan Ishlar Ro'yhati",
                'db_table': 'todos',
            },
        ),
        migrations.CreateModel(
            name='Instrument',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=128, verbose_name='Holati')),
                ('name', models.CharField(max_length=128, verbose_name='Instrument Nomi')),
                ('owner', models.ForeignKey(default=-1, on_delete=django.db.models.deletion.SET_DEFAULT, to='kozyap.brigadier', verbose_name='Brigadier')),
            ],
            options={
                'verbose_name': 'Uskuna',
                'verbose_name_plural': 'Uskunalar',
                'db_table': 'instrument',
            },
        ),
    ]
