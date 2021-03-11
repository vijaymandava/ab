# Generated by Django 3.1.5 on 2021-01-08 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CmToCustomerPostAssayStatusRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('instr_id', models.CharField(blank=True, max_length=9)),
                ('lims_id', models.CharField(blank=True, max_length=200)),
                ('serial_number', models.CharField(blank=True, max_length=9)),
                ('elapsed_assay_time', models.CharField(blank=True, max_length=20)),
                ('status', models.CharField(blank=True, max_length=20)),
                ('status_flag', models.CharField(blank=True, max_length=300)),
                ('status_update_time', models.CharField(blank=True, max_length=64)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CmToCustomerPostAssayStatusResponse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('acknowledge', models.CharField(blank=True, max_length=20)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CmToCustomerPostCanceledRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('instr_id', models.CharField(blank=True, max_length=9)),
                ('lims_id', models.CharField(blank=True, max_length=200)),
                ('serial_number', models.CharField(blank=True, max_length=9)),
                ('canceled_on', models.DateTimeField(blank=True, null=True)),
                ('canceled_by', models.CharField(blank=True, max_length=30)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CmToCustomerPostCanceledResponse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('acknowledge', models.CharField(blank=True, max_length=20)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CmToCustomerPostCompletedRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('instr_id', models.CharField(blank=True, max_length=9)),
                ('lims_id', models.CharField(blank=True, max_length=200)),
                ('serial_number', models.CharField(blank=True, max_length=9)),
                ('completed_on', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CmToCustomerPostCompletedResponse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('acknowledge', models.CharField(blank=True, max_length=20)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CmToCustomerPostLoadedRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('instr_id', models.CharField(blank=True, max_length=9)),
                ('lims_id', models.CharField(blank=True, max_length=200)),
                ('serial_number', models.CharField(blank=True, max_length=9)),
                ('loaded_on', models.DateTimeField(blank=True, null=True)),
                ('loaded_by', models.CharField(blank=True, max_length=30)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CmToCustomerPostLoadedResponse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('acknowledge', models.CharField(blank=True, max_length=20)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CmToCustomerPostResultsOnApprovalRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('instr_id', models.CharField(blank=True, max_length=9)),
                ('lims_id', models.CharField(blank=True, max_length=200)),
                ('serial_number', models.CharField(blank=True, max_length=9)),
                ('sample_id', models.CharField(blank=True, max_length=20)),
                ('lot_batch_id', models.CharField(blank=True, max_length=7)),
                ('method_name', models.CharField(blank=True, max_length=15)),
                ('handling_rule_name', models.CharField(blank=True, max_length=15)),
                ('action_alert_level_name', models.CharField(blank=True, max_length=15)),
                ('cfu_count', models.CharField(blank=True, max_length=10)),
                ('mold_count', models.CharField(blank=True, max_length=10)),
                ('status', models.CharField(blank=True, max_length=20)),
                ('test_status', models.CharField(blank=True, max_length=20)),
                ('approval', models.CharField(blank=True, max_length=10)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CmToCustomerPostResultsOnApprovalResponse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('acknowledge', models.CharField(blank=True, max_length=20)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CmToCustomerPostResultsRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('instr_id', models.CharField(blank=True, max_length=9)),
                ('lims_id', models.CharField(blank=True, max_length=200)),
                ('serial_number', models.CharField(blank=True, max_length=9)),
                ('sample_id', models.CharField(blank=True, max_length=20)),
                ('lot_batch_id', models.CharField(blank=True, max_length=7)),
                ('method_name', models.CharField(blank=True, max_length=15)),
                ('handling_rule_name', models.CharField(blank=True, max_length=15)),
                ('action_alert_level_name', models.CharField(blank=True, max_length=15)),
                ('cfu_count', models.CharField(blank=True, max_length=10)),
                ('mold_count', models.CharField(blank=True, max_length=10)),
                ('status', models.CharField(blank=True, max_length=20)),
                ('test_status', models.CharField(blank=True, max_length=20)),
                ('approval', models.CharField(blank=True, max_length=10)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CmToCustomerPostResultsResponse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('acknowledge', models.CharField(blank=True, max_length=20)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CustomerToCmGetAssayDetailsRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('instr_id', models.CharField(blank=True, max_length=9)),
                ('lims_id', models.CharField(blank=True, max_length=200)),
                ('sample_id', models.CharField(blank=True, max_length=20)),
                ('serial_number', models.CharField(blank=True, max_length=9)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CustomerToCmGetAssayDetailsResponse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('instr_id', models.CharField(blank=True, max_length=9)),
                ('lims_id', models.CharField(blank=True, max_length=200)),
                ('cassette_id', models.CharField(blank=True, max_length=20)),
                ('serial_number', models.CharField(blank=True, max_length=9)),
                ('lot_batch_id', models.CharField(blank=True, max_length=7)),
                ('incubation_start', models.DateTimeField(blank=True, null=True)),
                ('incubation_end', models.DateTimeField(blank=True, null=True)),
                ('target_temperature', models.CharField(blank=True, max_length=5)),
                ('media_type', models.CharField(blank=True, max_length=20)),
                ('action_alert_level', models.CharField(blank=True, max_length=15)),
                ('ordered_on', models.DateTimeField(blank=True, null=True)),
                ('ordered_by', models.CharField(blank=True, max_length=30)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CustomerToCmGetAssayStatusRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('instr_id', models.CharField(blank=True, max_length=9)),
                ('lims_id', models.CharField(blank=True, max_length=200)),
                ('sample_id', models.CharField(blank=True, max_length=20)),
                ('serial_number', models.CharField(blank=True, max_length=9)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CustomerToCmGetAssayStatusResponse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('instr_id', models.CharField(blank=True, max_length=9)),
                ('lims_id', models.CharField(blank=True, max_length=200)),
                ('sample_id', models.CharField(blank=True, max_length=20)),
                ('status', models.CharField(blank=True, max_length=20)),
                ('loaded_on', models.DateTimeField(blank=True, null=True)),
                ('loaded_by', models.CharField(blank=True, max_length=30)),
                ('elapsed_assay_time', models.CharField(blank=True, max_length=20)),
                ('status_flag', models.CharField(blank=True, max_length=300)),
                ('status_update_time', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CustomerToCmPostCancelRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('instr_id', models.CharField(blank=True, max_length=9)),
                ('lims_id', models.CharField(blank=True, max_length=200)),
                ('serial_number', models.CharField(blank=True, max_length=9)),
                ('sample_id', models.CharField(blank=True, max_length=20)),
                ('lot_batch_id', models.CharField(blank=True, max_length=7)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CustomerToCmPostCancelResponse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(blank=True, max_length=20)),
                ('status_type', models.CharField(blank=True, max_length=50)),
                ('status_message', models.CharField(blank=True, max_length=500)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CustomerToCmPostOrderRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('instr_id', models.CharField(blank=True, max_length=9)),
                ('lims_id', models.CharField(blank=True, max_length=200)),
                ('serial_number', models.CharField(blank=True, max_length=9)),
                ('sample_id', models.CharField(blank=True, max_length=20)),
                ('lot_batch_id', models.CharField(blank=True, max_length=7)),
                ('method_name', models.CharField(blank=True, max_length=15)),
                ('handling_rule_name', models.CharField(blank=True, max_length=15)),
                ('action_alert_level_name', models.CharField(blank=True, max_length=15)),
                ('aal_cfu_threshold_alert', models.CharField(blank=True, max_length=4)),
                ('aal_cfu_threshold_action', models.CharField(blank=True, max_length=4)),
                ('aal_cfu_threshold_specification', models.CharField(blank=True, max_length=4)),
                ('aal_cfu_threshold_pass', models.CharField(blank=True, max_length=4)),
                ('comment', models.CharField(blank=True, max_length=60)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CustomerToCmPostOrderResponse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(blank=True, max_length=20)),
                ('status_type', models.CharField(blank=True, max_length=50)),
                ('status_message', models.CharField(blank=True, max_length=500)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
