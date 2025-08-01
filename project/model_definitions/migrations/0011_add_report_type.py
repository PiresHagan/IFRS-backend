# Generated by Django 3.2.12 on 2025-07-31 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('model_definitions', '0010_currency_lineofbusiness'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReportType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('modified_on', models.DateTimeField(auto_now=True, verbose_name='last updated')),
                ('batch_model', models.CharField(choices=[('PAA', 'PAA'), ('GMM', 'GMM'), ('VFA', 'VFA')], help_text='PAA, GMM, VFA', max_length=10)),
                ('report_type', models.CharField(choices=[('lrc_movement_report', 'LRC Movement Report'), ('lic_movement_report', 'LIC Movement Report'), ('insurance_revenue_expense_report', 'Insurance Revenue and Expense Report'), ('disclosure_report', 'Disclosure Report (DR)'), ('financial_statement_items_report', 'Financial Statement Items (FSI) Report'), ('coverage_units_report', 'Coverage Units Report'), ('premium_allocation_reconciliation', 'Premium Allocation Reconciliation'), ('loss_component_report', 'Loss Component Report'), ('discount_rate_reconciliation', 'Discount Rate Reconciliation'), ('experience_adjustment_report', 'Experience Adjustment Report'), ('reinsurance_report', 'Reinsurance Report'), ('underlying_assumption_summary', 'Underlying Assumption Summary'), ('reconciliation_to_gaap_report', 'Reconciliation to GAAP Report'), ('csm_rollforward_report', 'CSM Rollforward Report'), ('risk_adjustment_rollforward', 'Risk Adjustment Rollforward'), ('csm_sensitivity_report', 'CSM Sensitivity Report')], help_text='Type of report', max_length=100)),
                ('is_enabled', models.BooleanField(default=True, help_text='Whether this report type is enabled')),
                ('notes', models.TextField(blank=True, help_text='Additional notes about this report type')),
            ],
            options={
                'verbose_name': 'Report Type',
                'verbose_name_plural': 'Report Types',
                'ordering': ['batch_model', 'report_type'],
                'unique_together': {('batch_model', 'report_type')},
            },
        ),
    ]
