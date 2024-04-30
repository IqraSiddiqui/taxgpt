from django.db import models

class W2Data(models.Model):
    Employee_SSA_number = models.CharField(max_length=100, null=True, blank=True)
    Employee_address = models.CharField(max_length=255, null=True, blank=True)
    Employee_name = models.CharField(max_length=100, null=True, blank=True)
    Employer_FED_ID = models.CharField(max_length=100, null=True, blank=True)
    Gross_Pay = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    Local_income_tax = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    Medicare_tax = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    Social_Security = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    State_income_tax = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    State_employer_state_id = models.IntegerField(null=True, blank=True)
    State_wages = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    Tax_withheld = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
