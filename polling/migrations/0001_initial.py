# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-08-17 06:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactLogging',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_datetime', models.DateTimeField(blank=True, null=True)),
                ('end_datetime', models.DateTimeField(blank=True, null=True)),
                ('measurement', models.FloatField(blank=True, null=True)),
                ('interval', models.FloatField(blank=True, default=6000, null=True)),
            ],
            options={
                'db_table': 'contact_logging',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='HospitalSubjectDeviceRegistration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_detail', models.TextField()),
                ('subject_insurance_policy_detail', models.TextField(blank=True, null=True)),
                ('medical_history_brief', models.TextField(blank=True, null=True)),
                ('device_details', models.TextField(blank=True, null=True, verbose_name='Device DataSheet')),
                ('lastupdate', models.DateTimeField(auto_now_add=True, db_column='LastUpdate')),
            ],
            options={
                'db_table': 'hospital_subject_device_registration',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='HospitalSubjectRegistration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hospital_detail', models.TextField(blank=True, null=True)),
                ('api_public_key', models.CharField(max_length=222)),
                ('api_private_key', models.CharField(blank=True, max_length=222, null=True)),
                ('api_consumer_key', models.CharField(blank=True, max_length=222, null=True)),
                ('api_token_key', models.CharField(blank=True, max_length=222, null=True)),
                ('isactive', models.IntegerField(blank=True, db_column='isActive', null=True)),
                ('isverified', models.IntegerField(blank=True, db_column='isVerified', null=True)),
                ('lastupdate', models.DateTimeField(auto_now_add=True, db_column='LastUpdate')),
            ],
            options={
                'db_table': 'hospital_subject_registration',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='InsuraceOfficeRegistration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('insurance_office', models.CharField(blank=True, max_length=100, null=True)),
                ('api_private_key', models.CharField(blank=True, max_length=200, null=True)),
                ('api_public_key', models.CharField(blank=True, max_length=200, null=True)),
                ('api_consumer_key', models.CharField(blank=True, max_length=200, null=True)),
                ('api_token_key', models.CharField(blank=True, max_length=200, null=True)),
                ('lastupdate', models.DateTimeField(auto_now_add=True, db_column='LastUpdate')),
            ],
            options={
                'db_table': 'insurace_office_registration',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Insuranceplancategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('insuranceplancategoryname', models.CharField(blank=True, db_column='InsurancePlanCategoryName', max_length=200, null=True)),
                ('insuranceplancategorydocumention', models.TextField(blank=True, db_column='InsurancePlanCategoryDocumention', null=True)),
                ('lastupdate', models.DateTimeField(auto_now_add=True, db_column='LastUpdate')),
            ],
            options={
                'db_table': 'insuranceplancategory',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='InsurancePremiumModelling',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hospital_id', models.IntegerField(blank=True, null=True)),
                ('subject_id', models.IntegerField(blank=True, null=True)),
                ('insurance_policy_id', models.IntegerField(blank=True, null=True)),
                ('projected_premium', models.FloatField(blank=True, null=True)),
                ('lastupdate', models.DateTimeField(auto_now_add=True, db_column='LastUpdate')),
            ],
            options={
                'db_table': 'insurance_premium_modelling',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='PublishSubscribeContact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datastreamidentifier', models.CharField(db_column='DataStreamIdentifier', max_length=300)),
                ('documentation', models.TextField(db_column='Documentation')),
                ('startcollect', models.IntegerField(blank=True, db_column='StartCollect', null=True)),
                ('dateofcreation', models.DateTimeField(db_column='DateofCreation')),
                ('createbyid', models.IntegerField(blank=True, db_column='CreateByID', null=True)),
                ('intervalofpull', models.FloatField(blank=True, db_column='IntervalofPull', null=True)),
                ('lastupdate', models.DateTimeField(auto_now_add=True, db_column='LastUpdate')),
                ('InsuraceOfficeid', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='polling.InsuraceOfficeRegistration')),
                ('hospital_subject_device_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='polling.HospitalSubjectDeviceRegistration')),
            ],
            options={
                'db_table': 'publish_subscribe_contact',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='SensorDeviceType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('devicename', models.CharField(blank=True, max_length=200, null=True)),
                ('devicefunction', models.CharField(blank=True, max_length=200, null=True)),
                ('measurement_unit', models.CharField(blank=True, max_length=50, null=True)),
                ('documentation', models.CharField(blank=True, max_length=400, null=True)),
                ('lastupdate', models.DateTimeField(auto_now_add=True, db_column='LastUpdate')),
            ],
            options={
                'db_table': 'sensor_device_type',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='hospitalsubjectdeviceregistration',
            name='hospital_name_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='polling.HospitalSubjectRegistration'),
        ),
        migrations.AddField(
            model_name='contactlogging',
            name='contact',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='polling.PublishSubscribeContact'),
        ),
    ]