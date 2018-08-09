from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.
class Query(models.Model):
    product_choices = (
        ('HL', 'Home Loan'),
        ('LAP', 'Loan Against Property'),
        ('CV', 'Commercial Vehicle Loan'),
        ('SME', 'SME Loan'),
        ('Corporate', 'Corporate Loan'),
        ('Tractor', 'Tractor Loan'),
        ('AIB', 'Bulk AIB'),
    )
    rating_choices = (
        ('AAA','AAA'),
        ('AA', 'AA'),
        ('A', 'A'),
        ('BBB', 'BBB'),
        ('BB', 'BB'),
        ('U', 'Unrated'),
        ('CM', 'Capital Market'),
        ('CRE', 'CRE'),
        ('CRE_RH','CRE_RH'),
        ('RRE', 'RRE'),
        ('RRP','RRP')
    )
    typ = models.CharField(max_length=4, blank=False)
    ApplNo = models.CharField("Application Number", max_length=25,blank=False)
    RMName = models.CharField("RM's Name", max_length=150, blank=False)
    HRMS = models.CharField("HRMS No", max_length=7, blank=False)
    product = models.CharField("Product", max_length=10, blank=False,
                               choices=product_choices)
    sanction_amt = models.IntegerField("Loan Amount", validators=[MinValueValidator(0)],
                                       blank=False)
    roi = models.DecimalField("ROI", max_digits=4, decimal_places=2,
                              validators=[MinValueValidator(0)], blank=False)
    tenure = models.IntegerField("Tenure", blank=True, default=60,
                                 validators=[MinValueValidator(0)],)
    utilisation = models.DecimalField("Utilisation", max_digits=5, decimal_places=2, blank=True,
                              validators=[MinValueValidator(0)], default=70.0)
    ltv = models.DecimalField("LTV", max_digits=5, decimal_places=2, blank=True,
                              validators=[MinValueValidator(0)], default=0.0)
    rating = models.CharField("Rating", max_length=10, default=None, null=True,
                              blank=True, choices=rating_choices)
    profee = models.DecimalField(max_digits=4, decimal_places=2, blank=False,
                              validators=[MinValueValidator(0)])
    conpay = models.DecimalField("Sourcing Fee", max_digits=5, decimal_places=2, blank=False,
                              validators=[MinValueValidator(0)])
    insur = models.IntegerField("Insurance Premium", validators=[MinValueValidator(0)], blank=False)
    other = models.IntegerField("Other Income", validators=[MinValueValidator(0)], blank=True,
                                default=0)
    recurr = models.BooleanField("Is Other Income Recurring?")
    psl = models.BooleanField("Priority Sector Lending")
    agri_psl = models.BooleanField("Agri Priority Sector Lending")
    rrp = models.BooleanField("Is is RRP?", default=False)
    datetime = models.DateTimeField(auto_now=True)
    ip = models.CharField(default="0.0.0.0", max_length=15, blank=True)



