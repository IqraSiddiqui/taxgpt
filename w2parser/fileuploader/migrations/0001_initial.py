# Generated by Django 5.0.4 on 2024-04-29 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='W2Data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Employee_SSA_number', models.CharField(blank=True, max_length=100, null=True)),
                ('Employee_address', models.CharField(blank=True, max_length=255, null=True)),
                ('Employee_name', models.CharField(blank=True, max_length=100, null=True)),
                ('Employer_FED_ID', models.CharField(blank=True, max_length=100, null=True)),
                ('Gross_Pay', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('Local_income_tax', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('Medicare_tax', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('Social_Security', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('State_income_tax', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('State_employer_state_id', models.IntegerField(blank=True, null=True)),
                ('State_wages', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('Tax_withheld', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
            ],
        ),
    ]
